from typing import override


class Customer:
    def __init__(self, _name, _email, _id):
        self.name = _name
        self.email = _email
        self.__id = _id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value > 0:
            self.__id = value

    @override
    def __str__(self):
        return f"Customer {self.name} (ID:{self.__id}) -Email: {self.email}"

    @override
    def __repr__(self):
        return f"Customer(name='{self.name}', email= '{self.email}',id={self.__id}) "


if __name__ == '__main__':
    c1 = Customer("Alice", "alice@example.com", 101)
    c2 = Customer("Bob", "bob@example.com", 202)
    print(c1)
    print(repr(c2))
    c1.id = -5
    print("after id change attempt:", c1.id)
