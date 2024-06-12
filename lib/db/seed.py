#!usr/bin/env python
from ..models.store import Store
from ..models.department import Department
from ..models.product import Product


Store.drop_table()
Store.create_table()
Store.create("Mini Mall", "Athens Way")
Store.create("Mountain Mall", "Kilimanjaro")
Store.create("Target", "Boulevard St.")

Department.drop_table()
Department.create_table()
Department.create("Foods", "Food stuffs", 1)

Product.drop_table
Product.create_table()
Product.create("Pizza", "Food", 1)


