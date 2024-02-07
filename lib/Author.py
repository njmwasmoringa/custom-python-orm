from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

"""
This is the Student subclass that maps to students table
"""
class Author(BASE):
    
    __tablename__ = "authors"
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    contact = Column(String())