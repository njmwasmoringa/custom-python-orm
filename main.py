from lib.db import CURSOR, CONN
from lib import Student, Book, Author

if __name__ == "__main__":
    import ipdb
    print("This is main run directly")
    
    ipdb.set_trace()
    CONN.close()