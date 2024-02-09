from Student import Student
from db import session

def register_student(student_data):
    
    # We first save the student
    student = Student(**student_data)
    session.add(student)
    session.commit()
    
    # We pick the student id to add admission number and update
    student.admission_no = "STD-{:02d}".format(student.id)
    session.commit()
    
    return student
    