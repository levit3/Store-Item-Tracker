from models.__init__ import conn, cursor
from store import Store

class Department:
    def __init__(self, name, description, store_id, id = None):
        self.name = name
        self.description =description
        self.store_id = store_id
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        elif not 2 <= len(value) <= 15:
            raise Exception("Name must be between 2 and 15 characters")
        self._name = value
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('The description must be a string')
        elif not value:
            raise Exception("The description must not be empty")
        self._description = value
        
    @property
    def store_id(self):
        return self._store_id
    
    @store_id.setter
    def store_id(self, value):
        sql = """
            SELECT id
            FROM stores
            WHERE id = ?
        """
        id_ = cursor.execute(sql, (value,)).fetchone()
        
        if not id_:
            raise ValueError("The store id must be in the stores table")
        else:
            self._store_id = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT, 
                store_id FOREIGN KEY,
                FOREIGN KEY (store_id) REFERENCES stores(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments
        """
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql = """
            INSERT INTO departments(name, description, store_id)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.store_id))
        conn.commit()
        
    @classmethod    
    def create(cls, name, description, store_id):
        department = cls(name, description, store_id)
        department.save()
        return department