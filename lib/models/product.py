from .__init__ import conn, cursor

class Product:
    all = {}
    
    def __init__(self, name, product_type, department_id, id = None):
        self.name = name
        self.product_type = product_type
        self.department_id = department_id
        # self.store_id = store_id
        
    def __repr__(self):
        return f"<ID: {self.id}, Name: {self.name}, Product Type: {self.product_type}, Department ID: {self.department_id}>"
        
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
            self._name = value.title()
            
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
            
    # @property
    # def store_id(self):
    #     return self._store_id
    
    # @store_id.setter
    # def store_id(self, value):
    #     sql = """
    #         SELECT id
    #         FROM stores
    #         WHERE id = ?
    #     """
    #     id_ = cursor.execute(sql, (value, )).fetchone()
        
    #     if not id_:
    #         raise Exception("The store id must be in the stores table")
    #     else:
    #         self._store_id = value
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                product_type TEXT,
                department_id,
                FOREIGN KEY (department_id) REFERENCES departments(id)
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
            INSERT INTO products(name, product_type, department_id)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.product_type, self.department_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        sql = """
            UPDATE products
            SET name =?, product_type =?, department_id =?
            WHERE id =?
        """
        cursor.execute(sql, (self.name, self.product_type, self.department_id, self.id))
        conn.commit()
        
    @classmethod
    def create(cls, name, product_type, department_id):
        product = cls(name, product_type, department_id)
        product.save()
        return product
    
    @classmethod
    def instance_from_db(cls, row):
        product = cls.all.get(row[0])
        if product:
            product.name = row[1]
            product.product_type = row[2]
            product.department_id = row[3]
        else:
            product = cls(row[1], row[2], row[3])
            product.id = row[0]
            cls.all[product.id] = product
        return product
    
    @classmethod
    def find_by_id(cls, id_):
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """
        product = cursor.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(product) if product else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM products
            WHERE name = ?
        """
        products = cursor.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(product) for product in products] if products else None
    
    @classmethod
    def find_by_type(cls, type_):
        sql = """
            SELECT *
            FROM products
            WHERE product_type = ?
        """
        products = cursor.execute(sql, (type_, )).fetchall()
        return [cls.instance_from_db(product) for product in products]
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """
        products = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(product) for product in products]
        
    @classmethod
    def get_all_in_department_id(cls, department_id):
        sql = """
            SELECT *
            FROM products
            WHERE department_id = ?
        """
        products = cursor.execute(sql, (department_id,)).fetchall()
        return [cls.instance_from_db(product) for product in products] if products else None
    
    @classmethod
    def get_all_in_department_name(cls, name):
        sql = """
            SELECT *
            FROM products
            INNER JOIN departments
            ON products.department_id = departments.id
            WHERE departments.name = ?
        """
        products = cursor.execute(sql, (name, )).fetchall()
        return [cls.instance_from_db(product) for product in products] if products else None
        