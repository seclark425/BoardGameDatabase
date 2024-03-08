from linked_set import linked_set
from boardgame import boardgame
import shelve

class home_collection(linked_set):
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    

    def add(self, new_entry):
        linked_set.add(self, new_entry)
        self.save(new_entry)
    
    def save(self, new_entry: boardgame):
        home_file = shelve.open(f'{self.__name}_home', flag = 'c')
        new_data = [new_entry]
        home_file[f'{new_entry.get_id()}'] = new_data
        home_file.close()
        

new_home = home_collection("John")
new_home.add(5)
new_home.add(7)

print(new_home.to_array())

