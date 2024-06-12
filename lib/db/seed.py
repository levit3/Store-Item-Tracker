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

Department.create("Produce", "Fresh fruits and vegetables", 1)
Department.create("Animal Produce", "Meat, eggs", 1)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 1)
Department.create("Bakery", "Freshly baked goods", 1)
Department.create("Household", "Cleaning supplies and household essentials", 1)
Department.create("Clothing", "All types of clothes eg sweater, socks etc.", 1)
Department.create("Electronics", "Electronic devices and accessories", 1)
Department.create("Toys", "Children's toys and games", 1)

Department.create("Produce", "Fresh fruits and vegetables", 2)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 2)
Department.create("Bakery", "Freshly baked goods", 2)
Department.create("Household", "Cleaning supplies and household essentials", 2)

Department.create("Produce", "Fresh fruits and vegetables", 3)
Department.create("Animal Produce", "Meat, eggs", 3)
Department.create("Dairy", "Dairy products such as milk, cheese, and yogurt", 3)
Department.create("Bakery", "Freshly baked goods", 3)
Department.create("Books", "Books", 3)
Department.create("Household", "Cleaning supplies and household essentials", 3)

Department.create("Laptops", "Various brands and models of laptops", 4)
Department.create("Smartphones", "Latest smartphones and accessories", 4)
Department.create("Gaming", "Gaming consoles, accessories, and games", 4)
Department.create("Accessories", "Tech accessories such as chargers, cables, and cases", 4)



Product.drop_table()
Product.create_table()

Product.create("Apple", "Fruit", 100, 1)
Product.create("Orange", "Fruit", 80, 1)
Product.create("Chicken", "Meat", 50, 2)
Product.create("Beef", "Meat", 60, 2)
Product.create("Milk", "Dairy", 40, 3)
Product.create("Cheese", "Dairy", 30, 3)
Product.create("Bread", "Bakery", 70, 4)
Product.create("Toothpaste", "Household", 120, 5)
Product.create("T-shirt", "Clothing", 90, 6)
Product.create("Smartphone", "Electronics", 20, 7)
Product.create("Lego Set", "Toys", 25, 8)

Product.create("Banana", "Fruit", 110, 9)
Product.create("Grapes", "Fruit", 85, 9)
Product.create("Yogurt", "Dairy", 45, 10)
Product.create("Butter", "Dairy", 18, 10)
Product.create("Baguette", "Bakery", 75, 11)
Product.create("Dish Soap", "Household", 130, 12)

Product.create("Strawberry", "Fruit", 100, 13)
Product.create("Blueberry", "Fruit", 90, 13)
Product.create("Eggs", "Animal Produce", 55, 14)
Product.create("Cream", "Dairy", 65, 15)
Product.create("Croissant", "Bakery", 85, 16)
Product.create("Book: Fiction", "Books", 50, 17)
Product.create("Book: Non-Fiction", "Books", 40, 17)
Product.create("Vacuum Cleaner", "Household", 30, 18)

Product.create("MacBook Pro", "Laptops", 35, 19)
Product.create("Dell XPS 13", "Laptops", 20, 19)
Product.create("iPhone 13", "Smartphones", 30, 20)
Product.create("Samsung Galaxy S21", "Smartphones", 25, 20)
Product.create("PlayStation 5", "Gaming", 23, 21)
Product.create("Xbox Series X", "Gaming", 19, 21)
Product.create("Nintendo Switch", "Gaming", 30, 21)
Product.create("Wireless Charger", "Accessories", 40, 22)
Product.create("USB-C Cable", "Accessories", 50, 22)
Product.create("Bluetooth Headphones", "Accessories", 35, 22)
Product.create("Gaming Mouse", "Accessories", 22, 22)
Product.create("External Hard Drive", "Accessories", 28, 22)
Product.create("HDMI Cable", "Accessories", 60, 22)
Product.create("Smartwatch", "Accessories", 17, 22)
Product.create("Laptop Sleeve", "Accessories", 14, 22)
