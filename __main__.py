from item.item import Item, ItemInputs
from pulumi import export


def main():
    item = Item("foo", ItemInputs("777", "J4NN0"))

    export("item_id", item.item_id)
    export("name", item.name)


if __name__ == '__main__':
    main()
