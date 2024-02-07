from .db import BASE
from sqlalchemy import Column, Integer, DateTime, String

"""
This is the Student subclass that maps to students table
"""
class Student(BASE):
    
    __tablename__ = "students"
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    gender = Column(String())
    grade = Column(Integer())
    birthday = Column(DateTime())
    admission_no = Column(Integer())
        
    def read(self, book):
        print("Readding", book)