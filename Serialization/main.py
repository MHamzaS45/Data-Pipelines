#main.py
from file_handler import FileHandler
from item import Item

class Main():
    def __init__(self):
        filename = "Serialization\\inventory.csv"
        inventory_file = FileHandler(filename)
        rows = inventory_file.read()
        print("### inventory ###") 
        inventory: list[Item] = []
        for row in rows:
            _item = Item.deserialize(row)
            _item.display_price()
            inventory.append(_item)
        print("### inventory ###")
        feed = input(f"Change item value (enter 1 - {len(inventory) - 1}): ")
        print(f" You chose item {feed}")
        try:
            index = int(feed) - 1
            feed = input(f"Set new value for {inventory[index].name}: ")
            inventory[index].set_value(float(feed))                          
        except Exception:
            print("Invalid input. Please enter a number corresponding to an item.")
        print("Serializing items into rows.")
        print("## Rows ##")
        for _item in inventory:
            row = _item.serialize()
            rows.append(row)
            print(row)
        print(f"Saving items into {filename}")
        inventory_file.write(rows)
        print("## Rows ##")


if __name__ == "__main__":
    main = Main()
