class linked_set:
    def __init__(self) -> None:
        self.__head = None
        self.__number_of_entries = 0
    
    
    def add(self, new_entry):
        """adds entry, return true if successful and false if not"""
        if self.contains(new_entry):
            return False
        else:
            new_node = self.node(new_entry)
            temp = self.__head
            self.__head = new_node
            self.__head.set_next(temp)
            self.__number_of_entries += 1
            return True

    def remove(self):
        """remove random entry, returning the entry removed"""
        temp = self.__head
        self.__head = self.__head.get_next()
        temp.set_next(None)
        self.__number_of_entries -= 1
        return temp
    
    def remove_entry(self, entry):
        """remove specific entry, return true if it was found and removed,
        and false if it was not"""
        curr = self.__head
        while (curr is not None):
            if curr.get_data() == entry:
                curr.set_data(self.__head.get_data())
                temp = self.__head
                self.__head = self.__head.get_next()
                temp.set_next(None)
                self.__number_of_entries -= 1
                return True
            curr = curr.get_next()
        return False
    
    def contains(self, entry):
        """searches chain for specific entry, returning true if the
        chain contains it and false if it does not"""
        curr = self.__head
        
        while curr is not None:
            if curr.get_data() == entry:
                return True
            else:
                curr = curr.get_next()
        return False
    
    def number_of_entries(self):
        return self.__number_of_entries
    
    def to_array(self):
        curr = self.__head
        array = []
        
        while curr is not None:
            temp = [curr.get_data()]
            array += temp
            curr = curr.get_next()
        return array

    class node:

        def __init__(self, data, next=None) -> None:
            self.__data = data
            self.__next = next
        
        def get_next(self):
            return self.__next

        def set_next(self, next):
            self.__next = next
        
        def set_data(self, new_entry):
            self.__data = new_entry
        
        def get_data(self):
            return self.__data