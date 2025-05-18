from typing import override
class Student:
    # def __int__(self):
    #     self.name = ""
    #     self.height = ""
    #     self.weight = ""
    #     self.age = ""
    #     self.address = ""
    def __init__(self,_name,_height,_weight,_age,_address)->None:
        self.name=_name
        self.height = _height
        self.weight = _weight
        self.age = _age
        self.address = _address

    def __str__(self)->str:
        return f"{self.name},{self.age},{self.address},{self.address},{self.weight},{self.height}"

    def __repr__(self)->str:
        return f"Student({self.name},{self.age},{self.address},{self.address},{self.weight},{self.height})"



