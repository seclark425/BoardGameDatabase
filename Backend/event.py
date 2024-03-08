from linked_set import linked_set
from home import home_collection

class event(linked_set):
    def __init__(self, host: home_collection=None):
        self.__host = host
        if host is not None:
            home_array = host.to_array()
            for each in home_array:
                self.add(each)

    def get_host_games(self) -> home_collection:
        return self.__host
    

    
