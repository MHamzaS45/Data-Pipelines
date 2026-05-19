#main.py
from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename) #create an object
rows = inventory_file.read() #Use read method for the previously created object
print(f"\n####{filename}####")
for row in rows:
    #print(row)
    #dont have to call static method with an instance of the class
    #can call it directly on the class itself   
    item = Item.deserialize(row)
    item.display_price()
print(f"####{filename}####")
