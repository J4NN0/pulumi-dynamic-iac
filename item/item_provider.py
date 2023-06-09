from pulumi.dynamic import *


class _ItemProviderInputs(object):
    """
    It is the unwrapped version of the same inputs from the ItemInputs class.
    """
    item_id: str
    name: str

    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name


class ItemProvider(ResourceProvider):
    """
    Dynamic resource provider to CRUD a new kind of custom resource
    """

    def check(self, _olds: _ItemProviderInputs, news: _ItemProviderInputs) -> CheckResult:
        """
        It is invoked before any other methods. It has two jobs and it verifies that the inputs (particularly the news)
        are valid or return useful error messages if they are not.
        :param _olds: old input properties that were stored in the state file after the previous update to the resource
        :param news: new inputs from the current deployment
        :return: set of checked inputs
        """

        failures = []

        for key in {**news}:
            value = {**news}[key]
            if not value:
                failures.append(CheckFailure(property_=key, reason="Property's value cannot be emtpy"))

        return CheckResult(inputs={**news}, failures=failures)

    def create(self, inputs: _ItemProviderInputs) -> CreateResult:
        """
        It is invoked when the URN of the resource is not found in the existing state of the deployment.
        :param inputs: inputs to be created
        :return: a set of outputs from the backing provider
        """

        # Call your external provider (e.g. HTTP POST to create entity)
        return CreateResult(id_=inputs["item_id"], outs={**inputs})

    def update(self, _id: str, _olds: _ItemProviderInputs, _news: _ItemProviderInputs) -> UpdateResult:
        """
        It is invoked if the call to diff indicates that a replacement is necessary.
        :param _id: id of the resource as returned by create method
        :param _olds: old outputs from the checkpoint file
        :param _news: new checked inputs from the current deployment
        :return: new set of outputs
        """

        # Call your external provider (e.g. HTTP PUT/PATCH to update entity)
        return UpdateResult({**_news})

    def delete(self, _id: str, _props: _ItemProviderInputs) -> None:
        """
        It is invoked if the URN exists in the previous state but not in the new desired state, or if a replacement
        is needed. The method deletes the corresponding resource from the cloud provider.
        :param _id: id of the resource as returned by create method
        :param _props: the old outputs from the checkpoint file
        """

        # Call your external provider (e.g. HTTP DELETE to delete entity)
        pass
