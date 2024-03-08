from home import home_collection
from boardgame import boardgame

class User:

    def __init__(self, name: str):
        self.__name = name
        self.__homes = {}
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name
    
    def get_homes(self) -> dict:
        return self.__homes

    def add_home(self, collection: home_collection):
        self.__homes[f"{collection.get_name()}"] = collection
    
    def add_game(home: home_collection, game: boardgame):
        home.add(game)

    
