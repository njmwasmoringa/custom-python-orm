from .db import CONN, CURSOR

""" This is the super class that contains all the ORM operations
    and will be inherited by the child class which repesent 
    tables

Returns:
    _type_: _description_
"""
class Model:
    
    def __init__(self, table_name, create_table_query) -> None:
        id = None
        Model.table_name = table_name
        Model.create_table_query = create_table_query
        
        Model.create_table()
    
    def save(self):
        columns = self.__dict__.keys()
        data = tuple(self.__dict__.values())
        sql = "INSERT INTO %s(%s) VALUES(%s)" % \
            (Model.table_name, ",".join(columns), ",".join(["?"] * len(columns)))
        
        CURSOR.execute(sql, data)
        last_insert_sql = "SELECT last_insert_rowid() FROM %s" % (Model.table_name)
        self.id = CURSOR.execute(last_insert_sql).fetchone()[0]
        CONN.commit()
    
    @classmethod
    def create(cls, row):
        print(row)
        row = cls(**row)
        row.save()
        return cls.new_from_db(list(row.__dict__.values()))
        
    
    @classmethod
    def new_from_db(cls, row):
        columns = cls.table_columns()
        data_dict = {}
        
        for i in range(len(columns)):
            data_dict[columns[i]] = row[i]
        
        return data_dict
    
    @classmethod
    def table_columns(cls):
        columns_sql = "PRAGMA table_info(%s)" % (cls.table_name)
        return [column[1] for column in CURSOR.execute(columns_sql).fetchall()]        
    
    @classmethod
    def get_all(cls):
        columns = cls.table_columns()
        sql = "SELECT %s FROM %s" % (",".join(columns), cls.table_name)        
        all = CURSOR.execute(sql).fetchall()
        return [ cls.new_from_db(row) for row in all ]
    
    @classmethod
    def get_by_prk(cls, id):
        sql = "SELECT * FROM %s WHERE id = %s" % (cls.table_name, id)
        row = CURSOR.execute(sql).fetchone()
        return row
    
    @classmethod
    def create_table(cls):
        CURSOR.execute(cls.create_table_query)
        CONN.commit()