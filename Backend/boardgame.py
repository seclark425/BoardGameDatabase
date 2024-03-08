import typing

class boardgame:

    def __init__(self, id, title) -> None:
        self.__name = title
        self.__id = id
        self.__expansion = False
        self.__weight = 0

    def set_id(self, num: int):
        self.__id = num
    
    def get_id(self) -> int:
        return self.__id
    
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def get_name(self) -> str:
        return self.__name
    
    def set_expansion(self, boolean: bool):
        self.__expansion = boolean
    
    def get_expansion(self) -> bool:
        return self.__expansion
    
    def set_weight(self, new_weight: float):
        self.__weight = new_weight
    
    def get_weight(self) -> float:
        return self.__weight
    
    def set_pic(self, link: str):
        self.__pic = link
    
    def get_pic(self) -> str:
        return self.__pic
    
    def set_description(self, text: str):
        self.__description = text
    
    def get_description(self) -> str:
        return self.__description
    
    def set_min(self, min: int):
        self.__min = min
    
    def get_min(self) -> int:
        return self.__min
    
    def set_max(self, max: int):
        self.__max = max
    
    def get_max(self) -> int:
        return self.__max

    

    # def get_weight_10_point(original):
    #     new = -0.733 * (original) ** 2 + 6.9 * (original) - 6.167
    #     if new > 10:
    #         return float(10)
    #     else:
    #         return new
