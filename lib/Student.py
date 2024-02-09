from db import BASE
from sqlalchemy import Column, Integer, DateTime, String, CheckConstraint

"""
This is the Student subclass that maps to students table
"""
class Student(BASE):
    
    __tablename__ = "students"
    __table_args__ = (
        CheckConstraint("grade BETWEEN 1 AND 12", "grade_between_1_and_12"),
    )
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(60))
    email = Column(String(55), unique=True)
    gender = Column(String(10))
    grade = Column(Integer())
    birthday = Column(DateTime())
    admission_no = Column(Integer())
        
    def read(self, book):
        print("Readding", book)