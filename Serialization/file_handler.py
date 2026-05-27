#file_handler.py

from fileinput import filename


class FileHandler:
    filepath: str
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        return None


    def read(self) -> list[str]:
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8") # open file for reading 
            row = filehandle.readline() 
            while row != '':
              rows.append(row.rstrip('\n'))
              row = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f" '{self.filepath}' was not readable. Please try again.")
            exit(-1) # from sys library
        return rows
    
    def write(self, rows):
        try:
         filehandle = open(self.filepath, 'w', encoding="UTF-8")
         for row in rows:
            filehandle.write(row + "\n")
            filehandle.close()
        except Exception:
            print(f"Error saving to file '{self.filepath}'. Please try again.")
        print("Program Ending..")
    