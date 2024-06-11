from models.__init__ import conn, cursor
from store import Store

class Store:
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
            raise Exception("THe description must not be empty")
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
    