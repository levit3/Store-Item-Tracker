from models.__init__ import conn, cursor

class Product:
    def __init__(self, name, product_type, department_id, store_id, id = None):
        self.name = name
        self.product_type = product_type
        self.department_id = department_id
        self.store_id = store_id
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Product name must be a string")
        elif not value:
            raise Exception("Product name must not be empty")
        else:
            self._name = value
            
    @property
    def product_type(self):
        return self._product_type
    
    @product_type.setter
    def product_type(self, value):
        if not isinstance(value, str):
            raise ValueError("Product type must be a string")
        elif not value:
            raise Exception("Product type name must not be empty")
        else:
            self._product_type = value
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, value):
        sql = """
            SELECT id
            FROM departments
            WHERE id = ?
        """
        id_ = cursor.execute(sql, (value, )).fetchone()
        
        if not id_:
            raise Exception("The department id must be in the department table")
        else:
            self._department_id = value
            
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
        id_ = cursor.execute(sql, (value, )).fetchone()
        
        if not id_:
            raise Exception("The store id must be in the stores table")
        else:
            self._store_id = value
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IT NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                product_type TEXT,
                department_id FOREIGN KEY,
                store_id FOREIGN KEY,
                FOREIGN KEY (department_id) REFERENCES departments(id),
                FOREIGN KEY (store_id) REFERENCES stores(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products
        """
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql = """
            INSERT INTO products(name, product_type, department_id, store_id)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.product_type, self.department_id, self.store_id))
        conn.commit()
        self.id = cursor.lastrowid
        
    @classmethod
    def create(cls, name, product_type, department_id, store_id):
        product = cls(name, product_type, department_id, store_id)
        product.save()
        return product
    
            
            
        