
class Person:
    def __init__(self,_name,_height,_weight):
        self.name=_name
        self.height=_height
        self.weight=_weight

    def print_details(self):
        print(f"the name is: '{self.name}'")

    def print_measurements(self):
        print(f"the height is: {self.height}(cm)")
        print(f"the weight is: {self.weight}(kg)")
