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
        
    
    
            
            
        