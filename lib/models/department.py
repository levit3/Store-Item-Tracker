from .__init__ import conn, cursor
from .store import Store

class Department:
    all = {}
    def __init__(self, name, description, store_id, id = None):
        self.name = name
        self.description =description
        self.store_id = store_id
        
    def __repr__(self):
        return f"<ID: {self.id}, Name: {self.name}, Description: {self.description}, Store ID: {self.store_id}>"
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        elif not 2 <= len(value) <= 15:
            raise Exception("Name must be between 2 and 15 characters")
        self._name = value.title()
        
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
                store_id,
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
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
    
    def delete(self, id):
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        cursor.execute(sql, (id,))
        conn.commit()
        
        del type(self).all[id]
        self.id = None
        
    def update(self):
        sql = """"
            UPDATE departments
            SET name =?, description =?, store_id =?,
            WHERE id =?
        """
        cursor.execute(sql, (self.name, self.description, self.store_id, self.id))
        conn.commit()
        
    @classmethod    
    def create(cls, name, description, store_id):
        department = cls(name, description, store_id)
        department.save()
        return department
    
    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = row[1]
            department.description = row[2]
            department.store_id = row[3]
        else:
            department = cls(row[1], row[2], row[3])
            department.id = row[0]
            cls.all[department.id] = department
        
        return department
    
    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT *
            FROM departments
            WHERE id = ?
        """
        department = cursor.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(department) if department else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM departments
            WHERE name = ?
        """
        departments = cursor.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(department) for department in departments] if departments else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM departments
        """
        departments = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(department) for department in departments]
        
    @classmethod
    def find_by_store_id(cls, store_id):
        sql = """
            SELECT *
            FROM departments
            WHERE store_id = ?
            """
        departments = cursor.execute(sql, (store_id,)).fetchall()
        return [cls.instance_from_db(department) for department in departments] if departments else None

    @classmethod
    def find_by_store_name(cls, name):
        sql = """
            SELECT *
            FROM departments
            INNER JOIN stores
            ON departments.store_id = stores.id
            WHERE stores.name = ?
        """
        departments = cursor.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(department) for department in departments] if departments else None
    