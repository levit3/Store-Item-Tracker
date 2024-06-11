from .__init__ import conn, cursor
class Store:
    all = {}
    
    def __init__(self, name, location, id = None):
        self.name = name
        self.location = location
        
    def __repr__(self):
        return f"<ID: {self.id}, Store: {self.name}, Location: {self.location}>"
        
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
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                location TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS stores
        """
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql = """
            INSERT INTO stores (name, location)
            VALUES (?, ?)
        """
        
        cursor.execute(sql, (self.name, self.location))
        conn.commit()
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, location):
        store = cls(name, location)
        store.save()
        return store
    
    def delete(self, id):
        sql = """
            DELETE FROM stores
            WHERE id = ?
        """
        cursor.execute(sql, (id,))
        conn.commit()
        
        del type(self).all[id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        store = cls.all.get(row[0])
        if store:
            store.name = row[1]
            store.location = row[2]
        else:
            store = cls(row[1], row[2])
            store.id = row[0]
            cls.all[store.id] = store
        return store
    
    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT *
            FROM stores
            WHERE id = ?
        """
        store = cursor.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(store) if store else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM stores
            WHERE name = ?
        """
        store = cursor.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(store) if store else None
    
    @classmethod
    def find_in_location(cls, location):
        sql = """
            SELECT *
            FROM stores
            WHERE location = ?
        """
        stores = cursor.execute(sql, (location,)).fetchall()
        return [cls.instance_from_db(store) for store in stores]
    
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM stores
        """
        stores = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(store) for store in stores]
        
    
        
        