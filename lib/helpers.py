from models.store import Store
from models.department import Department
from models.product import Product

### STORE OPERATIONS ###
def add_new_store():
    name = input("Enter the name of the new store: ")
    location = input("Enter the location of the new store: ")
    if name and location:
        try:
            store = Store.create(name, location)
            return store
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def remove_store():
    id_ = input("Enter the id of the store: ")
    if id_.isdigit():
        store = Store.find_by_id(int(id_))
        if store:
            choice = input(f"Are you sure you want to remove {store}? (y/n): ")
            if choice.lower() == "y":
                store.delete()
            elif choice.lower() == "n":
                print(f"\nOperation cancelled")
            else:
                print("\t>>>> Invalid choice <<<<")
        else:
            print(f"\t>>>> No store with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def update_store():
    id_ = input("Enter the store id: ")
    if id_.isdigit():
        store = Store.find_by_id(int(id_))
        if store:
            try:
                name = input("Enter the new store name: ")
                store.name = name
                location = input("Enter the new store location: ")
                store.location = location
                store.update()
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            print(f"\t>>>> No store with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_store_by_id():
    id_ = input("Enter the store id: ")
    if id_.isdigit():
        store = Store.find_by_id(int(id_))
        if store:
            print(f"\n{store}\n")
        else:
            print(f"\t>>>> Store with id {id_} not found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_store_by_name():
    name = input("Enter the store name: ")
    if name:
        store = Store.find_by_name(name)
        if store:
            print(f"\n{store}\n")
        else:
            print(f"\t>>>> Store with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def find_store_by_location():
    location = input("Enter the location: ")
    if location:
        stores = Store.find_in_location(location.title())
        if stores:
            for store in stores:
                print(f"{store}")
        else:
            print(f"\t>>>> No stores found in {location} <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def view_all_stores():
    stores = Store.get_all()
    for store in stores:
        print(store)

def view_all_store_departments_id():
    id_ = input("Enter the store id: ")
    if id_.isdigit():
        departments = Department.find_by_store_id(int(id_))
        if departments:
            for department in departments:
                print(department)
        else:
            print(f"\t>>>> No departments found in store with id {id_} <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def view_all_store_departments_name():
    name = input("Enter the store name: ")
    if name:
        departments = Department.find_by_store_name(name.title())
        if departments:
            for department in departments:
                print(department)
        else:
            print(f"No department with the name {name} was found")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

### DEPARTMENT OPERATIONS ###
def new_department():
    name = input("Enter the name of the new department: ")
    description = input("Enter the description: ")
    store_id = input("Enter the store id: ")
    if name and description and store_id.isdigit():
        department = Department.create(name, description, int(store_id))
        return department
    else:
        print(f"\t>>>> Input cannot be blank and store ID must be an integer <<<<")

def delete_department():
    id_ = input("Enter the department id: ")
    if id_.isdigit():
        department = Department.find_by_id(int(id_))
        if department:
            choice = input(f"Are you sure you want to remove {department}? (y/n): ")
            if choice.lower() == "y":
                department.delete()
            elif choice.lower() == "n":
                print(f"\nOperation cancelled")
            else:
                print("\t>>>> Invalid choice <<<<")
        else:
            print(f"\t>>>> No department with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_department_by_id():
    id_ = input("Enter the department id: ")
    if id_.isdigit():
        department = Department.find_by_id(int(id_))
        if department:
            print(f"\n{department}\n")
        else:
            print(f"\t>>>> Department with id {id_} not found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_department_by_name():
    name = input("Enter the department name: ")
    if name:
        departments = Department.find_by_name(name.title())
        if departments:
            for department in departments:
                print(f"{department}")
        else:
            print(f"\t>>>> Department with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def view_all_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def update_department():
    id_ = input("Enter the department id: ")
    if id_.isdigit():
        department = Department.find_by_id(int(id_))
        if department:
            try:
                name = input("Enter the new department name: ")
                department.name = name
                description = input("Enter the new department description: ")
                department.description = description
                store_id = input("Enter the new store id: ")
                department.store_id = int(store_id) if store_id.isdigit() else department.store_id
                department.update()
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            print(f"\t>>>> No department with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

### PRODUCT OPERATIONS ###
def new_product():
    name = input("Enter the name of the new product: ")
    description = input("Enter the description: ")
    quantity = input("Enter the quantity of the product: ")
    department_id = input("Enter the department id: ")
    if name and description and quantity.isdigit() and department_id.isdigit():
        try:
            product = Product.create(name, description, int(quantity), int(department_id))
            return product
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    else:
        print(f"\t>>>> Input cannot be blank and IDs must be integers <<<<")

def delete_product():
    id_ = input("Enter the product id: ")
    if id_.isdigit():
        product = Product.find_by_id(int(id_))
        if product:
            choice = input(f"Are you sure you want to remove {product}? (y/n): ")
            if choice.lower() == "y":
                product.delete()
            elif choice.lower() == "n":
                print(f"\nOperation cancelled")
            else:
                print("\t>>>> Invalid choice <<<<")
        else:
            print(f"\t>>>> No product with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def update_product():
    id_ = input("Enter the product id: ")
    if id_.isdigit():
        product = Product.find_by_id(int(id_))
        if product:
            try:
                name = input("Enter the new product name: ")
                product.name = name
                type_ = input("Enter the new product type: ")
                product.type = type_
                quantity = input("Enter the product quantity: ")
                product.quantity = int(quantity) if quantity.isdigit() else product.quantity
                department_id = input("Enter the new department id: ")
                product.department_id = int(department_id) if department_id.isdigit() else product.department_id
                product.update()
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            print(f"\t>>>> No product with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_product_by_id():
    id_ = input("Enter the product id: ")
    if id_.isdigit():
        product = Product.find_by_id(int(id_))
        if product:
            print(f"\n{product}\n")
        else:
            print(f"\t>>>> Product with id {id_} not found <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def find_product_by_name():
    name = input("Enter the product name: ")
    if name:
        products = Product.find_by_name(name.title())
        if products:
            for product in products:
                print(f"{product}")
        else:
            print(f"\t>>>> Product with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def view_all_products():
    products = Product.get_all()
    for product in products:
        print(product)

def view_all_products_in_department_id():
    id_ = input("Enter the department id: ")
    if id_.isdigit():
        products = Product.get_all_in_department_id(int(id_))
        if products:
            for product in products:
                print(product)
        else:
            print(f"\t>>>> No products were found in department with id {id_} <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def view_all_products_in_department_name():
    name = input("Enter the department name: ")
    if name:
        products = Product.get_all_in_department_name(name.title())
        if products:
            for product in products:
                department = Department.find_by_id(product.id)
                store = Store.find_by_id(department.store_id)
                print(f"\n{store.name}")
                print(f"{product}")
        else:
            print(f"\t>>>> Department with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def products_in_store_id():
    id_ = input("Enter Store ID: ")
    if id_.isdigit():
        departments = Department.find_by_store_id(int(id_))
        if departments:
            store = Store.find_by_id(int(id_))
            print(f"\n{store.name}")
            for department in departments:
                print(f"{department.name}")
                print(f"{department.id}")
                products = Product.get_all_in_department_id(department.id)
                for product in products:
                    print(product)
        else:
            print(f"\t>>>> Store with id {id_} does not exist <<<<")
    else:
        print(f"\t>>>> Input must be a valid integer <<<<")

def products_in_store_name():
    name = input("Enter Store Name: ").title()
    if name:
        departments = Department.find_by_store_name(name)
        if departments:
            store = Store.find_by_name(name)
            print(f"\n{store.name}")
            for department in departments:
                print(f"{department.name}")
                products = Product.get_all_in_department_name(department.name)
                for product in products:
                    print(product) if product else print("None")
        else:
            print(f"\t>>>> Store with name {name} does not exist <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def show_almost_out():
    products = Product.get_all()
    for product in products:
        if 0 < product.quantity <= 10:
            department = Department.find_by_id(product.department_id)
            store = Store.find_by_id(department.store_id)
            print(f"{store.name}")
            print(f"***{product.name} is almost out of stock. Only {product.quantity} remaining!***\n")
        elif product.quantity == 0:
            department = Department.find_by_id(product.department_id)
            store = Store.find_by_id(department.store_id)
            print(f"{store.name}")
            print(f"***{product.name} is out of stock!!***\n")
            
            
def update_quantity():
    product_name = input("Enter the product name: ")
    if not product_name.isdigit():
        products = Product.find_by_name(product_name)
        if products:
            store_name = input("Enter the name of the store you would like to update stock: ")
            if not store_name.isdigit():
                store = Store.find_by_name(store_name)
                if store:
                    for product in products:
                            department = Department.find_by_id(product.department_id)
                            store = Store.find_by_id(department.store_id)
                            if store.name == store_name:
                                print(f"Current stock for {product.name} is {product.quantity}\n")
                                if product.quantity > 0:
                                    question = input("Enter 'u' to to update quantity for the day or 's' to stock up: ")
                                else:
                                    question = input("Enter 's' to stock up: ") 
                                if question.lower() == "u" and product.quantity > 0:
                                    if product.quantity > 0:
                                        quantity = input("Enter the number items sold today: ")
                                        if quantity.isdigit() and int(quantity) > 0:
                                            prev = product.quantity
                                            product.quantity -= int(quantity)
                                            product.update()
                                            print(f"{product.name} stock has been updated from {prev} to {product.quantity}\n")
                                        else:
                                            print(f"\n{quantity} must be a valid integer\n")
                                    else:
                                        print(f"\n{product.name} is out of stock\n")
                                elif question.lower() == "s":
                                    quantity = input("Enter the number of items to stock up: ")
                                    if quantity.isdigit() and int(quantity) > 0:
                                        prev = product.quantity
                                        product.quantity += int(quantity)
                                        product.update()
                                        print(f"\n{product.name} stock has been updated from {prev} to {product.quantity}\n")
                                    else:
                                        print(f"\n{quantity} must be a valid integer\n")
                                else:
                                    print(f"\t>>>> Invalid input <<<<")
                            else:
                                print(f"\t>>>> Product {product.name} does not exist in the stock of {store.name} <<<<")
                else:
                    print(f"\t>>>> Store with name {store_name} does not exist <<<<")
            else:
                print(f"\t>>>> Input must be a string <<<<")
        else:
            print(f"\t>>>> Product with name {product_name} does not exist <<<<")
    else:
        print(f"\t>>>> Input must be a string <<<<")

### QUIT ###
def quit():
    st = "*" * (len("Store manager") + 6)
    print(f"\t      {st}")
    print(f"\t       **Store manager**")
    print(f"\t      {st}")
    exit()
