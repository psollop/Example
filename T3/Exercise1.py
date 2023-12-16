import math

class Person:
    def __init__(self, name, surname, age, address, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = str(phone_number)  # Convert phone_number to string

    def copy(self):
        new_person = Person(self.name, self.surname, self.age, self.address, self.phone_number)
        return new_person

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = str(phone_number)

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nAddress: {self.address}\nPhone Number: {self.phone_number}"

# Example usage of the Person class:
person = Person("Daniel", "M", 30, "123 Main St", "555-123-4567")
person1 = Person("Daniel", "M", 30, "123 Main St", 123456)

copy = person.copy()
copy.set_age(18)

print(person.get_age())

print(person.__str__())

value = math.pi

print(value.__str__())

# The __del__ method is not needed and is omitted

# You can also use the getters and setters to access and modify attributes:
person.set_age(35)
print(f"Updated Age: {person.get_age()}")
