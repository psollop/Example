class Publication:
    def __init__(self, title, authors, year, status):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status

    def __str__(self):
        return f" Title: {self.title}, year: {self.title} by {', '.join(self.authors)}"

class Book(Publication):
    def __init__ (self, title, authors, year, status, isbn, num_pages):
        super().__init__(self,title,authors,year,status)
        self.isbn = isbn
        self.num_pages = num_pages 

class Journal(Publication):
    def __init__(self,title,authors,year,status, edition_number,periodicity):
        super().__init__(self,title,authors,year,status)
        self.edition_number = edition_number
        self.periodicity = periodicity

class User:
    def __init__(self,name,userID,max_pubs):
        self.name = name
        self.userID = userID
        self.pubs = []
        self.max_pubs = max_pubs

    def lend_pub(self,Publication):
        if len(self.pubs) < self.max_pubs:
            self.lend_pub.append(Publication)