Create in Python library system that handles publications, users, and the library system itself. The system should include the following classes with their respective attributes and methods:
- Publication: This is the base class Book AND Magazine will inherit.
Attributes: title ( str), authors ( list of str), year of publication (int), status ("available", "borrowed")
- Book: inherits from publication
Attributes isbn(str of length 13, digits only), number of pages(int)
-Journal( inherits from publication)
Attributes edition number: int, periodicity: str
-User: Professor and Student inherit from this class.
    Attributes name(str), user_id(str of length 9, digits only), pubs(list of publication)
    Methods: 
    - lend_pub(Publication): Adds a Publication to the publications list. It has to change the Book status.
    - return_pub(Publication) Removes a Publication to the publications list. It has to change the book status.

-Professor(inherits from User):
Attributes: department:str, employee_id(str of length 6), max_pubs =2

-Student(inherits from User):
Attributes: grade:str, student_id(str of length 6), max_pubs =1

-Library:
Attributes: name(str), catalogue(a list of publication objects), list of users (a list of users objects).object
Methods:
    - show catalogue(): Shows the objects in the library catalogue.
    -add_publication(Publication): Adds a new publication to the catalogue
    - register_user(User): Register a new user in the library.
    - lend_pub(User, Publication): Auser can borrow a publication from the catalogue. It should check that both the user and the Publication are registered. This method should modify the publication status and update the User's list of publication ( as long as their maimum number of publication allows).
    - return_pub(User, Publication): Allows a user to return a borrowed publication. tHIS METHOD should modify the publication status and update the User's list of publications.


TEST CODE
library = Library("Loyola Andalucía Library")
book1 =Book("Learning Python II", ["Javier Perez", "Daniel Muñoz"], 2023, "1234567890123", 300)
journal1= Journal("Technology Journal", ["Stephen Curry", "Lebron James"], 2022, 7, "Annual")
journal2= Journal("Medical Journal", ["Michael Jordan", "Larry Bird"], 2023, 5, "Monthly")
professor1= Professor("Professor Tija", "123456789", "Philosophy", "123456")
student1=Student("Ashkabos Teberio", "987654321", "DAN", "654321")
student2=Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

library.add_publication(book1)
library.add_publication(journal1)
library.add_publication(journal2)
library.register_user(professor1)
library.register_user(student1)

library.show_catalogue()
library.lend_pub(professor1,book1)
library.lend_pub(student1,book1) #the book should be borrowed
print(student1.pubs) # empty list
library.return_pub(professor1,book1)
library.lend_pub(student1,book1) #the book should be available now
library.lend_pub(student1, journal2)
print(student1.pubs)
library.lend_pub(student2,journal1) # user not registered

Output:
Catalogue of the library: Loyola Andalucía Library
-------------------------------------------------------
(show catalogue)
--------------------------------------------------------
The book learning python II has been lent to professor tija
The book learning python II is not available
[]
The book learning python II was returned by professor tija
The book learning python II has been lent to Ashkabos Teberio
Ashkabos Teberio has reached the maximum limit of borrowed items
[learning python II- ['Javier perez', 'Daniel Muñoz'] (2023)]
The user or publication is not registered
