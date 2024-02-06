from .Model import Model

"""
    This is the Author subclass that maps to authors table
"""
class Author(Model):
    table_name = "authors"
    create_table_query = """
        CREATE TABLE IF NOT EXISTS authors(
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT
        )
    """
    
    def __init__(self, name, address) -> None:
        super().__init__(Author.table_name, Author.create_table_query)
        self.name = name
        self.address = address