
from dataclasses import dataclass # comes from the standard library module dataclasses. Have to be imported.


@dataclass
class Item:
 SEPARATOR = ","  # Define a class-level constant for the separator used in serialization. Uppercase by convention.
 # The @dataclass decorator will automatically create an __init__
 # method that initializes the following attributes.
 name: str
 value: float
 category: str
 weight: float

 @staticmethod        
 # The @staticmethod decorator is used to define a method that      
 # belongs to the class rather than an instance of the class. This
 # means you can call the method on the class itself, without
 # needing to create an instance. Can be used in place of @dataclass method
 def deserialize(row: str) -> 'Item':
 # Expecting row that contains => "name",value,"category",weight
 # The deserialize method is a static method that takes a string row as
 # input and returns an Item object.
 # It splits the input string row using the SEPARATOR (a comma in this
 # case) and assigns the resulting values to the corresponding
 # attributes of the Item class.
   columns = row.split(Item.SEPARATOR) # Serves to split the input string row into a list of values based on the defined SEPARATOR. 
   item = Item(
   columns[0], # name
   float(columns[1]), # value
   columns[2], # category
   float(columns[3]), # weight
   ) 
   return item

 def display_price(self) -> None:
   print(f"{self.name} costs {self.value} €. with a weight of {self.weight} kg.")
   return None

 def set_value(self, new_value: float) -> None:
  if new_value < 0:
    print("Value cannot be negative. Please enter a valid price.")
    return None
  else:
    self.value = new_value
    print(f"{self.name} now costs {self.value} €.")  
    return None
  
 def serialize(self) -> str:
    columns: list[str] = []
    columns.append(self.name)
    columns.append(str(self.value))
    columns.append(self.category)
    columns.append(str(self.weight))
    row = ','.join(columns)
