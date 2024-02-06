from .Model import Model

"""
This is the Student subclass that maps to students table
"""
class Student(Model):
    
    table_name = "students"
    create_table_query = """
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT,
                gender TEXT,
                level TEXT,
                admission_no INTEGER
            )
        """
    
    def __init__(self, name, gender, level, admission_no):
        super().__init__(Student.table_name, Student.create_table_query)
        self.name = name
        self.gender = gender
        self.level = level
        self.admission_no = admission_no
        
    def read(self, book):
        print("Readding", book)