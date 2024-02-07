from lib.db import BASE, engine, session
from lib import Student, Book, Author
from datetime import datetime

if __name__ == "__main__":
    import ipdb
    print("This is main run directly")
    
    BASE.metadata.create_all(engine)
    
    """ student1 = Student(
            name="Julius", 
            gender="Male", 
            grade=6, 
            birthday=datetime(year=2012, month=4, day=12),
            admission_no=234234
    )
    session.add(student1) """
    # session.query(Student).update()
    # session.commit()
    
    ipdb.set_trace()