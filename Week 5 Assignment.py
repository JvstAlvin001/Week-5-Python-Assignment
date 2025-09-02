# Base class (Encapsulation + Inheritance)
class Animal:
    def __init__(self, name, age):
        # Encapsulation: private attributes with "__"
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, new_age):
        if new_age >= 0:  # validation
            self.__age = new_age
        else:
            print("Age cannot be negative!")

    # Method meant to be overridden (Polymorphism)
    def move(self):
        print(f"{self.__name} is moving...")


# Subclass Dog (Inheritance + Polymorphism)
class Dog(Animal):
    def move(self):
        print(f"{self.get_name()} is running 🐕")


# Subclass Bird
class Bird(Animal):
    def move(self):
        print(f"
