from item.item_provider import ItemProvider
from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import *
from typing import Optional


class ItemInputs(object):
    item_id: Input[str]
    name: Input[str]

    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name


class Item(Resource):
    item_id: Output[str]
    name: Output[str]

    def __init__(self, name: str, props: ItemInputs, opts: Optional[ResourceOptions] = None):
        """
        Pulumi dynamic custom resource
        :param name: pulumi's resource name
        :param props: resource-specific arguments
        :param opts: optional options
        """

        super().__init__(ItemProvider(), name, {**vars(props)}, opts)
