from db import BASE
from sqlalchemy import Column, Integer, String, ForeignKey

"""
This is the Student subclass that maps to students table
"""
class Book(BASE):
    
    __tablename__ = "books"
    
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    author_id = Column(Integer(), ForeignKey("authors.id"))