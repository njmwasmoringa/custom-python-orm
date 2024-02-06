from .Model import Model

"""
    This is the child class for Book that maps to books table
"""
class Book(Model):
    table_name = "books"
    create_table_query = """
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER
            )
        """
        
    def __init__(self, title, author) -> None:
        super().__init__(Book.table_name, Book.create_table_query)
        self.title = title
        self.author_id = author.id
        
    