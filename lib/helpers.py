from models.store import Store
from models.department import Department
from models.product import Product


### STORE OPERATIONS ###
def add_new_store():
    name = input("Enter the name of the new store: ")
    location = input("Enter the location of the new store: ")
    store = Store.create(name, location)
    return store

def remove_store():
    id_ = input("Enter the id of the store:  ")
    store = Store.find_by_id(id_)
    if store:
        choice = input(f"Are you sure you want to remove {store}? (y/n):  ")
        if choice.lower() == "y":
            store.delete()
        elif choice.lower() == "n":
            print(f"\nOperation cancelled")
        else:
            print("\t>>>> Invalid choice <<<<")
    else:
        print(f"\t>>>> No store with id {id_} was found <<<<")

def update_store():
    id_ = input("Enter the store id:  ")
    if store := Store.find_by_id(id_):
        try:
            name = input("Enter the new store name: ")
            store.name = name
            location = input("Enter the new store location: ")
            store.location = location
            store.update()
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    elif id_:
        print(f"\t>>>> No store with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")
        
def find_store_by_id():
    id_ = input("Enter the store id:  ")
    store = Store.find_by_id(id_)
    if store:
        print(f"\n{store}\n")
    else:
        print(f"\t>>>> Store with id {id_} not found <<<<")

def find_store_by_name():
    name = input("Enter the store name:  ")
    store = Store.find_by_name(name)
    if store:
        print(f"\n{store}\n")
    else:
        print(f"\t>>>> Store with the name {name} not found <<<<")

def find_store_by_location():
    location = input("Enter the location:  ")
    stores = Store.find_in_location(location.title())
    if stores:
        for store in stores:
            print(f"{store}")
    else:
        print(f"\t>>>> No stores found in {location} <<<<")

def view_all_stores():
    stores = Store.get_all()
    for store in stores:
        print(store)

def view_all_store_departments_id():
    id_ = int(input("Enter the store id: "))
    if departments := Department.find_by_store_id(id_):
        for department in departments:
            print(department)
    else:
        print(f"\t>>>> No departments found in store with id {id_} <<<<")
    
def view_all_store_departments_name():
    name = input("Enter the store name: ")
    departments = Department.find_by_store_name(name.title())
    if departments:
        for department in departments:
            print(department)
    else:
        print(f"No department with the name {name} was found")
    
    
### DEPARTMENT OPERATIONS    ### 
def new_department():
    name = input("Enter the name of the new department: ")
    description = input("Enter the description: ")
    store_id = input("Enter the store id: ")
    department = Department.create(name, description, store_id)
    return department

def delete_department():
    id_ = input("Enter the department id:  ")
    department = Department.find_by_id(id_)
    if department:
        choice = input(f"Are you sure you want to remove {department}? (y/n):  ")
        if choice.lower() == "y":
            department.delete()
        elif choice.lower() == "n":
            print(f"\nOperation cancelled")
        else:
            print("\t>>>> Invalid choice <<<<")
    else:
        print(f"\t>>>> No department with id {id_} was found <<<<")
    
def find_department_by_id():
    id_ = input("Enter the department id:  ")
    department = Department.find_by_id(id_)
    if department:
        print(f"\n{department}\n")
    else:
        print(f"\t>>>> Department with id {id_} not found <<<<")

def find_department_by_name():
    name = input("Enter the department name:  ")
    departments = Department.find_by_name(name.title())
    if departments:
        for department in departments:
            print(f"{department}")
    else:
        print(f"\t>>>> Department with the name {name} not found <<<<")

def view_all_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def update_department():
    id_ = input("Enter the department id:  ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the new department name: ")
            department.name = name
            description = input("Enter the new department description: ")
            department.description = description
            store_id = input("Enter the new store id: ")
            department.store_id = store_id
            department.update()
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    elif id_:
        print(f"\t>>>> No department with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")
        

### PRODUCT OPERATIONS ###
def new_product():
    name = input("Enter the name of the new product: ")
    description = input("Enter the description: ")
    department_id = input("Enter the department id: ")
    product = Product.create(name, description, department_id)
    return product

def delete_product():
    id_ = input("Enter the product id:  ")
    product = Product.find_by_id(id_)
    if product:
        choice = input(f"Are you sure you want to remove {product}? (y/n):  ")
        if choice.lower() == "y":
            product.delete()
        elif choice.lower() == "n":
            print(f"\nOperation cancelled")
        else:
            print("\t>>>> Invalid choice <<<<")
    else:
        print(f"\t>>>> No product with id {id_} was found <<<<")
        
def update_product():
    id_ = input("Enter the product id:  ")
    if product := Product.find_by_id(id_):
        try:
            name = input("Enter the new product name: ")
            product.name = name
            type_ = input("Enter the new product type: ")
            product.type = type_
            department_id = input("Enter the new department id: ")
            product.department_id = department_id
            product.update()
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    elif id_:
        print(f"\t>>>> No product with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def find_product_by_id():
    id_ = input("Enter the product id:  ")
    product = Product.find_by_id(id_)
    if product:
        print(f"\n{product}\n")
    elif id_:
        print(f"\t>>>> Product with id {id_} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def find_product_by_name():
    name = input("Enter the product name:  ")
    products = Product.find_by_name(name.title())
    if products:
        for product in products:
            print(f"{product}")
    elif name:
        print(f"\t>>>> Product with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")


def view_all_products():
    products = Product.get_all()
    for product in products:
        print(product)

def view_all_products_in_department_id():
    id_ = int(input("Enter the department id: "))
    if products := Product.get_all_in_department_id(id_):
        for product in products:
            print(product)
    elif id_:
        print(f"\t>>>> No products were found in department  with id {id_} <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")

def view_all_products_in_department_name():
    name = input("Enter the product name:  ")
    products = Product.get_all_in_department_name(name.title())
    if products:
        for product in products:
            print(f"{product}")
    elif name:
        print(f"\t>>>> Product with the name {name} not found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")
        
def products_in_store_id():
    id_ = int(input("Enter Store ID: "))
    departments = Department.find_by_store_id(id_)
    for department in departments:
        print(f"\n{department.name}")
        products = Product.get_all_in_department_id(department.id)
        for product in products:
                print(product)

def products_in_store_name():    
    name = input("Enter Store Name: ").title()
    # store_name = Store.find_by_name(name)
    # print(store_name.name)
    departments = Department.find_by_store_name(name)
    
    for department in departments:
        print(f"\n{department.name}")
        products = Product.get_all_in_department_name(department.name)
        for product in products:
            print(product) if product else print("Nun")
    
### QUIT ###
def quit():
    st = "*" * (len("Store manager") + 6)
    print(f"\t      {st}")
    print(f"\t       **Store manager**")
    print(f"\t      {st}")
    exit()
