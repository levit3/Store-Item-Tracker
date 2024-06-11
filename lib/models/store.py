from models.__init__ import conn, cursor
class Store:
    def __init__(self, name, location, id = None):
        self.name = name
        self.location = location
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        elif not 3 <= len(value) <= 15:
            raise Exception("Name must be between 3 and 15 characters")
        self._name = value
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('Location must be a string')
        elif not value:
            raise Exception("Location must not be empty")
        self._location = value
        
    def __repr__(self):
        return f"<ID: {self.id}, Store: {self.name}, Location: {self.location}>"
    
    @classmethod
    def create_table():
        sql = """
            CREATE TABLE IF NOT EXISTS stores(
                id PRIMARY KEY AUTOINCREMENT
                name TEXT
                location TEXT
            );
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def drop_table():
        sql = """
            DROP TABLE IF EXISTS stores
        """
        cursor.execute(sql)
        conn.commit()