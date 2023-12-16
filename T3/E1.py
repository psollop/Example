import math

class Person:
    def __init__(self,name,surname,age,address,phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = str(phone_number)

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name

    def get_surname(self):
        return self.surname
    
    def set_surname(self,surname):
        self.surname=surname

    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age=age

    def get_address(self):
        return self.address
    
    def set_address(self,address):
        self.address = address
    
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number (self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return f" Name: {self.name}, Surname {self.surname}, age: {self.age}, address: {self.address}, phone number: {self.phone_number}"
    
person = Person("Pablo", "Sollo", 20, "loyola", "666222333")

print(person)
print(person.get_age())

print(person.__str__())
person.set_age(35)
print(f"Updated Age: {person.get_age()}")
    
    


    