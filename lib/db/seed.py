#!usr/bin/env python
from ..models.store import Store
from ..models.department import Department
from ..models.product import Product


Store.drop_table()
Store.create_table()
Store.create("Mini Mall", "Athens Way")
Store.create("Mountain Mall", "Kilimanjaro")
Store.create("Target", "Boulevard St.")
Store.create("Best Buy", "Main Street")


Department.drop_table()
Department.create_table()
Department.create("Grocery", "Various grocery items", 1)
Department.create("Produce", "Fresh fruits and vegetables", 1)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 1)
Department.create("Bakery", "Freshly baked goods", 1)
Department.create("Household", "Cleaning supplies and household essentials", 1)
Department.create("Clothing", "All types of clothes eg sweater, socks etc.", 1)
Department.create("Electronics", "Electronic devices and accessories", 1)
Department.create("Toys", "Children's toys and games", 1)

Department.create("Grocery", "Various grocery items", 2)
Department.create("Produce", "Fresh fruits and vegetables", 2)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 2)
Department.create("Bakery", "Freshly baked goods", 2)
Department.create("Household", "Cleaning supplies and household essentials", 2)

Department.create("Grocery", "Various grocery items", 3)
Department.create("Produce", "Fresh fruits and vegetables", 3)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 3)
Department.create("Bakery", "Freshly baked goods", 3)
Department.create("Household", "Cleaning supplies and household essentials", 3)
Department.create("Home Goods", "Household items and appliances", 3)

Department.create("Laptops", "Various brands and models of laptops", 4)
Department.create("Smartphones", "Latest smartphones and accessories", 4)
Department.create("Gaming", "Gaming consoles, accessories, and games", 4)
Department.create("Accessories", "Tech accessories such as chargers, cables, and cases", 4)



Product.drop_table()
Product.create_table()

Product.create("Apple", "Fruit", 1)
Product.create("Orange", "Fruit", 1)
Product.create("Chicken", "Produce", 2)
Product.create("Beef", "Produce", 2)
Product.create("Milk", "Dairy", 3)
Product.create("Cheese", "Dairy", 3)
Product.create("Bread", "Bakery", 4)
Product.create("Toothpaste", "Household", 5)
Product.create("T-shirt", "Clothing", 6)
Product.create("Smartphone", "Electronics", 7)
Product.create("Lego Set", "Toys", 8)

Product.create("Apple", "Fruit", 9)
Product.create("Orange", "Fruit", 9)
Product.create("Banana", "Fruit", 9)
Product.create("Grapes", "Fruit", 9)
Product.create("Yogurt", "Dairy", 10)
Product.create("Butter", "Dairy", 10)
Product.create("Baguette", "Bakery", 11)
Product.create("Dish Soap", "Household", 12)

Product.create("Strawberry", "Fruit", 13)
Product.create("Blueberry", "Fruit", 13)
Product.create("Eggs", "Dairy", 14)
Product.create("Cream", "Dairy", 14)
Product.create("Croissant", "Bakery", 15)
Product.create("Book: Fiction", "Books", 16)
Product.create("Book: Non-Fiction", "Books", 16)
Product.create("Vacuum Cleaner", "Home Goods", 19)


