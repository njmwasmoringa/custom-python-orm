from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

"""
This is the Student subclass that maps to students table
"""
class Book(BASE):
    
    __tablename__ = "books"
    
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author_id = Column(Integer())