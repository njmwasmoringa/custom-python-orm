from datetime import datetime
from db import session
from models import Student, Book

students = session.query(Student).all()
books = session.query(Book).all()

navigation_menu = {
    1:{
        "request": "Student",
        "options": {
            1: {
                "request": "Registration",
                "action": "register_student",
                "fields": [{
                    "field": "name",
                    "instruction": "Enter student name"
                },{
                    "field": "email",
                    "instruction": "Enter student email"
                },{
                    "field": "gender",
                    "instruction": "Select gender"
                },{
                    "field": "grade",
                    "instruction": "Select grade between 1 and 12"
                },{
                    "field": "birthday",
                    "instruction": "Enter student birthday(DD/MM/YYYY)",
                    #Here we are using lamba(anonymous function) to format data
                    "func": lambda dateInput : datetime.strptime(dateInput, "%d/%m/%Y")
                }]
            },
            2: {
                "request": "Borrow a book",
                "action": "borrow_book",
                "fields": [{
                    "field": "student",
                    "instruction": "Select Student: \n %s" % "\n".join([ "%s: %s" % (student.id, student.name) for student in students])
                },{
                    "field": "book",
                    "instruction": "Select Book: \n %s" % "\n".join([ "%s: %s" % (book.id, book.title) for book in books])
                }]
            },
            3: {
                "request": "Generate Student Report"
            }
            
        }
    },
    2:{
        "request":"Author"
    }
}