from db import BASE
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Book import Book

"""
This is the Student subclass that maps to students table
"""
class Author(BASE):
    
    __tablename__ = "authors"
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    contact = Column(String(255))
    books= relationship("Book", backref="author")