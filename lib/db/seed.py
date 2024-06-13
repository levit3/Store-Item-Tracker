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

Department.create("Produce", "Fresh fruits and vegetables")
Department.create("Meat", "Meat products")
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt")
Department.create("Bakery", "Freshly baked goods")
Department.create("Household", "Cleaning supplies and household essentials")
Department.create("Clothing", "All types of clothes eg sweater, socks etc.")
Department.create("Electronics", "Electronic devices and accessories")
Department.create("Toys", "Children's toys and games")
Department.create("Books", "Books")
Department.create("Laptops", "Various brands and models of laptops")
Department.create("Smartphones", "Latest smartphones and accessories")
Department.create("Gaming", "Gaming consoles, accessories, and games")
Department.create("Accessories", "Tech accessories such as chargers, cables, and cases")




Product.drop_table()
Product.create_table()

Product.create("Apple", "Fruit", 100, 1, 1)
Product.create("Orange", "Fruit", 80, 1, 1)
Product.create("Chicken", "Meat", 50, 2, 1)
Product.create("Beef", "Meat", 60, 2, 1)
Product.create("Milk", "Dairy", 40, 3, 1)
Product.create("Cheese", "Dairy", 30, 3, 1)
Product.create("Bread", "Bakery", 70, 4, 1)
Product.create("Toothpaste", "Household", 120, 5, 1)
Product.create("T-shirt", "Clothing", 90, 6, 1)
Product.create("Smartphone", "Electronics", 20, 7, 1)
Product.create("Lego Set", "Toys", 25, 8, 1)

Product.create("Banana", "Fruit", 110, 1, 2)
Product.create("Grapes", "Fruit", 85, 1, 2)
Product.create("Yogurt", "Dairy", 45, 3, 2)
Product.create("Butter", "Dairy", 18, 3, 2)
Product.create("Baguette", "Bakery", 75, 4, 2)
Product.create("Dish Soap", "Household", 130, 5, 2)

Product.create("Strawberry", "Fruit", 100, 1, 3)
Product.create("Blueberry", "Fruit", 90, 1, 3)
Product.create("Eggs", "Meat", 55, 2, 3)
Product.create("Cream", "Dairy", 65, 3, 3)
Product.create("Croissant", "Bakery", 85, 4, 3)
Product.create("Book: Fiction", "Books", 50, 9, 3)
Product.create("Book: Non-Fiction", "Books", 40, 9, 3)
Product.create("Vacuum Cleaner", "Household", 30, 5, 3)

Product.create("MacBook Pro", "Laptops", 35, 10, 4)
Product.create("Dell XPS 13", "Laptops", 20, 10, 4)
Product.create("iPhone 13", "Smartphones", 30, 11, 4)
Product.create("Samsung Galaxy S21", "Smartphones", 25, 11, 4)
Product.create("PlayStation 5", "Gaming", 23, 12, 4)
Product.create("Xbox Series X", "Gaming", 19, 12, 4)
Product.create("Nintendo Switch", "Gaming", 30, 12, 4)
Product.create("Wireless Charger", "Accessories", 40, 13, 4)
Product.create("USB-C Cable", "Tech accessory", 50, 13, 4)
Product.create("Bluetooth Headphones", "Tech accessory", 35, 13, 4)
Product.create("Gaming Mouse", "Tech accessory", 22, 13, 4)
Product.create("External Hard Drive", "Tech accessory", 28, 13, 4)
Product.create("HDMI Cable", "Tech accessory", 60, 13, 4)
Product.create("Smartwatch", "Tech accessory", 17, 13, 4)
Product.create("Laptop Sleeve", "Tech accessory", 14, 13, 4)
