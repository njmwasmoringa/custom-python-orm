#! /usr/bin python3
from faker import Faker
from db import session
from Author import Author
from Book import Book

fakedata = Faker()

# Faker
# Genera 5 authors
author1 = Author(name="Guado", contact="213423lkj")
author2 = Author(name=fakedata.name(), contact=fakedata.address(), books=[])

session.add(author1)
session.add(author2)
session.commit()

# random books for each author
book1 = Book(title=fakedata.word(), author_id=author1.id)
book2 = Book(title=fakedata.word(), author_id=author1.id)


book3 = Book(title=fakedata.word(), author_id=author2.id)
book4 = Book(title=fakedata.word(), author_id=author2.id)
book5 = Book(title=fakedata.word(), author_id=author2.id)
book6 = Book(title=fakedata.word(), author_id=author2.id)

session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)

session.commit()