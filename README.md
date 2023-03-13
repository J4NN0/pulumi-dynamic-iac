# pulumi-dynamic-iac

Pulumi dynamic resource provider for custom Infrastructure as Code (IaC).

# Table of Contents

- [Usage](https://github.com/J4NN0/pulumi-dynamic-iac#usage)
- [Resources](https://github.com/J4NN0/pulumi-dynamic-iac#resources)

# Usage

1. Install Pulumi

       brew install pulumi/tap/pulumi

2. Clone repo

       git clone https://github.com/J4NN0/pulumi-dynamic-iac.git
       cd pulumi-dynamic-iac

3. Create a new Pulumi Stack

       pulumi stack init

    Not that if this is your first time running pulumi new or other pulumi commands, you may be prompted to log in to the Pulumi Service. After logging in, the CLI will proceed with walking you through creating a new stack:

   - You will be asked for a stack name. Hit `ENTER` to accept the default value of `dev`.

4. Deploy the Stack

       pulumi up

   This command evaluates your program and determines the resource updates to make.

   1. First, a preview is shown that outlines the changes that will be made when you run the update.
   2. Once the preview has finished, you are given three options to choose from. Choosing `details` will show you a rich diff of the changes to be made. Choosing `yes` will create your custom resource. Choosing `no` will return you to the user prompt without performing the update operation.

5. Destroy resources

       pulumi destroy

   To delete the Stack itself

       pulumi stack rm

   Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.

# Resources 

- [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
- [Pulumi Dynamic Providers](https://www.pulumi.com/docs/intro/concepts/resources/dynamic-providers/)
- [How Pulumi works](https://www.pulumi.com/docs/intro/concepts/how-pulumi-works/)
