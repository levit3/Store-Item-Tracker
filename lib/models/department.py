from .__init__ import conn, cursor
from .store import Store

class Department:
    all = {}
    DEPARTMENTS = ("Produce", "Meat", "Dairy", "Bakery", "Household", "Clothing", "Electronics", "Toys", "Books", "Laptops", "Smartphones", "Gaming", "Accessories", "Furniture", "Outdoor", "Beauty")

    def __init__(self, name, description, id = None):
        self.name = name
        self.description =description
        
    def __repr__(self):
        return f"<ID: {self.id}, Name: {self.name}, Description: {self.description}>"
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if value not in Department.DEPARTMENTS:
            raise Exception('Department must be one of the following: Produce, Meat, Dairy, Bakery, Household, Clothing, Electronics, Toys, Books, Laptops, Smartphones, Gaming, Accessories, Furniture, Outdoor, Beauty')
        elif not isinstance(value, str):
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

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT
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
            INSERT INTO departments(name, description)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.description))
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
        sql = """
            UPDATE departments
            SET name =?, description =?
            WHERE id =?
        """
        cursor.execute(sql, (self.name, self.description, self.id))
        conn.commit()
        
    @classmethod    
    def create(cls, name, description):
        department = cls(name, description)
        department.save()
        return department
    
    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.name = row[1]
            department.description = row[2]
        else:
            department = cls(row[1], row[2])
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
    def get_all_in_store_id(cls, store_id):
        sql = """
            SELECT DISTINCT departments.id, departments.name, departments.description
            FROM departments
            INNER JOIN products 
            ON departments.id = products.department_id
            WHERE products.store_id = ?
        """
        departments = cursor.execute(sql, (store_id,)).fetchall()
        return [cls.instance_from_db(department) for department in departments] if departments else None
    
    @classmethod
    def get_all_in_store_name(cls, name):
        sql = """
            SELECT DISTINCT departments.id, departments.name, departments.description
            FROM departments
            INNER JOIN products
            ON departments.id = products.department_id
            INNER JOIN stores
            ON products.store_id = stores.id
            WHERE stores.name =?
        """
        departments = cursor.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(department) for department in departments] if departments else None
    