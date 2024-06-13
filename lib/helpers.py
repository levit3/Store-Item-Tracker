from models.store import Store
from models.department import Department
from models.product import Product
import time
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.progress import track
console = Console()
### STORE OPERATIONS ###
def add_new_store():
    name = input("Enter the name of the new store: ")
    if name and not name.isdigit():
        location = input("Enter the location of the new store: ")
        if location and not location.isdigit():
            try:
                store = Store.create(name, location)
                print(f"\n{store} has been added successfully.")
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            console.print("\t>>>> Input cannot be blank <<<<", style="bold magenta dim")
    else:
        console.print("\t>>>> Input cannot be blank <<<<", style="bold magenta dim")

def remove_store():
    id_ = input("Enter the id of the store: ")
    if id_.isdigit() and int(id_) > 0:
        store = Store.find_by_id(int(id_))
        if store:
            choice = input(f"Are you sure you want to remove {store}? (y/n): ")
            if choice.lower() == "y":
                print(f"{store} has been removed")
                store.delete()
            elif choice.lower() == "n":
                console.print("Operation cancelled", style="bold dim magenta")
            else:
                console.print("\t>>>> Invalid choice <<<<", style="bold dim magenta")
        else:
           console.print(f"\t>>>> No store with id {id_} was found <<<<", style="bold dim blue")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def update_store():
    id_ = input("Enter the store id: ")
    if id_.isdigit() and int(id_) > 0:
        store = Store.find_by_id(int(id_))
        if store:
            try:
                name = input("Enter the new store name: ")
                if not name.isdigit():
                    store.name = name
                    location = input("Enter the new store location: ")
                    if not location.isdigit():
                        store.location = location
                        store.update()
                        print(f"{store} has been updated")
                    else:
                        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
                else:
                    console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
                
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
           console.print(f"\t>>>> No store with id {id_} was found <<<<", style="bold dim blue")

    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def find_store_by_id():
    id_ = input("Enter the store id: ")
    if id_.isdigit() and int(id_) > 0:
        store = Store.find_by_id(int(id_))
        if store:
            print(f"{store}")
        else:
            console.print(f"\t>>>> No store with id {id_} was found <<<<", style="bold dim blue")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def find_store_by_name():
    name = input("Enter the store name: ")
    if name and not name.isdigit():
        store = Store.find_by_name(name.title())
        if store:
            print(f"{store}")
        else:
            console.print(f"\t>>>> Store with the name {name} not found <<<<", style="dim blue bold")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

def find_store_by_location():
    location = input("Enter the location: ")
    if location and not location.isdigit():
        stores = Store.find_in_location(location.title())
        if stores:
            for store in stores:
                print(f"{store}")
        else:
            console.print(f"\t>>>> No stores found in {location} <<<<", style="bold dim blue")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

def view_all_stores():
    stores = Store.get_all()
    for store in stores:
        print(store)

def view_all_store_departments_id():
    id_ = input("Enter the store id: ")
    if id_.isdigit() and int(id_) > 0:
        departments = Department.get_all_in_store_id(int(id_))
        dept_list = []
        if departments:
            for department in departments:
                if department not in dept_list:
                    dept_list.append(department)
            for dept in dept_list:
                print(dept)
        else:
            console.print(f"\t>>>> No departments found in store with id {id_} <<<<", style="dim blue bold")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def view_all_store_departments_name():
    name = input("Enter the store name: ")
    if name and not name.isdigit():
        departments = Department.get_all_in_store_name(name.title())
        dept_list = []
        if departments:
            for department in departments:
                if department not in dept_list:
                    dept_list.append(department)
            for dept in dept_list:
                print(dept)
        else:
            console.print(f"\t>>>> No store with the name {name} was found <<<<", style="dim blue bold")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

### DEPARTMENT OPERATIONS ###
def new_department():
    name = input("Enter the name of the new department: ")
    if name and not name.isdigit():
        description = input("Enter the description: ")
        if description and not description.isdigit():
                department = Department.create(name, description)
                print(department)
        else:
            console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

        

def delete_department():
    id_ = input("Enter the department id: ")
    if id_.isdigit() and int(id_) > 0:
        department = Department.find_by_id(int(id_))
        if department:
            choice = input(f"Are you sure you want to remove {department}? (y/n): ")
            if choice.lower() == "y":
                print(f"{department} has been removed")
                department.delete()
            elif choice.lower() == "n":
                console.print("Operation cancelled", style="bold dim magenta")
            else:
                console.print("\t>>>> Invalid choice <<<<", style="bold dim magenta")
        else:
            console.print(f"\t>>>> No department with id {id_} was found <<<<", style="dim blue bold")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def find_department_by_id():
    id_ = input("Enter the department id: ")
    if id_.isdigit() and int(id_) > 0:
        department = Department.find_by_id(int(id_))
        if department:
            print(f"{department}")
        else:
            print(f"\t>>>> Department with id {id_} not found <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def find_department_by_name():
    name = input("Enter the department name: ")
    if name and not name.isdigit():
        departments = Department.find_by_name(name.title())
        if departments:
            for department in departments:
                print(f"{department}")
        else:
            console.print(f"\t>>>> No department with name {name} was found <<<<", style="dim blue bold")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

def view_all_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def update_department():
    id_ = input("Enter the department id: ")
    if id_.isdigit() and int(id_) > 0:
        department = Department.find_by_id(int(id_))
        if department:
            try:
                name = input("Enter the new department name: ")
                if name and not name.isdigit():
                    department.name = name
                    description = input("Enter the new department description: ")
                    if not description.isdigit():
                        department.description = description if description else department.description
                        department.update()
                        print(f"{department} has been updated")
                    else:
                        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
                else:
                    console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            console.print(f"\t>>>> No department with id {id_} was found <<<<", style="dim blue bold")

    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

### PRODUCT OPERATIONS ###
def new_product():
    name = input("Enter the name of the new product: ")
    if name and not name.isdigit():
        description = input("Enter the product type: ")
        if description and not description.isdigit():
            quantity = input("Enter the quantity of the product: ")
            if quantity.isdigit():
                department_id = input("Enter the department id: ")
                if department_id.isdigit():
                    store_id = input("Enter the store id: ")
                    if store_id.isdigit():
                        try:
                            product = Product.create(name, description, int(quantity), int(department_id), int(store_id))
                            print(f"{product} has been successfully added")
                        except Exception as exc:
                            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
                    else:
                        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")
                else:
                    console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")
            else:
                console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")
        else:
            console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")


def delete_product():
    id_ = input("Enter the product id: ")
    if id_.isdigit() and int(id_) > 0:
        product = Product.find_by_id(int(id_))
        if product:
            choice = input(f"Are you sure you want to remove {product}? (y/n): ")
            if choice.lower() == "y":
                print(f"\n{product} has been removed")
                product.delete()
            elif choice.lower() == "n":
                print(f"\nOperation cancelled")
            else:
                console.print("\t>>>> Invalid choice <<<<", style="bold dim magenta")
        else:
            print(f"\t>>>> No product with id {id_} was found <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def update_product():
    id_ = input("Enter the product id: ")
    if id_.isdigit() and int(id_) > 0:
        product = Product.find_by_id(int(id_))
        if product:
            try:
                name = input("Enter the new product name: ")
                product.name = name
                type_ = input("Enter the new product type: ")
                product.product_type = type_
                quantity = input("Enter the product quantity: ")
                product.quantity = int(quantity) if quantity.isdigit() else product.quantity
                department_id = input("Enter the new department id: ")
                product.department_id = int(department_id) if department_id.isdigit() else product.department_id
                store_id = input("Enter the new store id: ")
                product.store_id = int(store_id) if store_id.isdigit() else product.store_id
                product.update()
                print(f"{product} has been updated")
            except Exception as exc:
                print(f"\t>>>> Error: ", exc, "<<<<", "\n")
        else:
            print(f"\t>>>> No product with id {id_} was found <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def find_product_by_id():
    id_ = input("Enter the product id: ")
    if id_.isdigit() and int(id_) > 0:
        product = Product.find_by_id(int(id_))
        if product:
            print(f"{product}")
        else:
            print(f"\t>>>> Product with id {id_} not found <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

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
        console.print("\t>>>> Input cannot be blank <<<<", style="bold magenta dim")

def view_all_products():
    products = Product.get_all()
    for product in products:
        print(product)

def view_all_products_in_department_id():
    id_ = input("Enter the department id: ")
    if id_.isdigit() and int(id_) > 0:
        products = Product.get_all_in_department_id(int(id_))
        if products:
            products_by_store = {}
            for product in products:
                store = Store.find_by_id(product.store_id)
                if store.name not in products_by_store:
                    products_by_store[store.name] = []
                products_by_store[store.name].append(product)
            
            for store_name, products in products_by_store.items():
                print(f"\n{store_name}")
                for product in products:
                    print(product)
        else:
            print(f"\t>>>> No products were found in department with id {id_} <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def view_all_products_in_department_name():
    name = input("Enter the department name: ")
    if name and not name.isdigit():
        products = Product.get_all_in_department_name(name.title())
        if products:
            products_by_store = {}
            for product in products:
                store = Store.find_by_id(product.store_id)
                if store.name not in products_by_store:
                    products_by_store[store.name] = []
                products_by_store[store.name].append(product)
            
            for store_name, products in products_by_store.items():
                print(f"\n{store_name}")
                for product in products:
                    print(product)
        else:
            print(f"\t>>>> Department with the name {name} not found <<<<")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")


def products_in_store_id():
    id_ = input("Enter Store ID: ")
    if id_.isdigit() and int(id_) > 0:
        departments = Department.get_all_in_store_id(int(id_))
        if departments:
            store = Store.find_by_id(int(id_))
            print(f"\n{store.name}")
            for department in departments:
                print(f"\n{department.name}")
                products = Product.get_all_in_department_store_id(department.id, store.id)
                for product in products:
                    print(product)
        else:
            print(f"\t>>>> Store with id {id_} does not exist <<<<")
    else:
        console.print("\t>>>> Input must be a valid integer <<<<", style="dim bold magenta")

def products_in_store_name():
    name = input("Enter Store Name: ").title()
    if name and not name.isdigit():
        departments = Department.get_all_in_store_name(name)
        if departments:
            store = Store.find_by_name(name)
            print(f"\n{store.name}")
            for department in departments:
                print(f"\n{department.name}")
                products = Product.get_all_in_department_store_id(department.id, store.id)
                for product in products:
                    print(product) if product else print("None")
        else:
            print(f"\t>>>> Store with name {name} does not exist <<<<")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

def show_almost_out():
    console = Console()
    products = Product.get_all()
    ending_products = {}
    for product in products:
        if product.quantity <= 15:
            store = Store.find_by_id(product.store_id)
            ending_products[product.name] = [store.name, product.name, product.quantity]
            
    console.print("\n[bold red]-------------------------Stock Updates-----------------------[/bold red]")
    for name, data in ending_products.items():
            if data[2] > 0:
                print(data[0])
                print(f"***[bold dim magenta]{data[1]}[/] is almost out of stock. Only[bold red] {data[2]}[/bold red] remaining!***\n")
            else:
                print(data[0])
                print(f"***[bold dim red]{data[1]}[/] is out of stock!!***\n")
    print("[bold red]------------------------------------------------------------[/bold red]\n")
            
def update_quantity():
    product_name = input("Enter the product name: ")
    if not product_name.isdigit():
        products = Product.find_by_name(product_name.title())
        if products:
            store_name = input("Enter the name of the store you would like to update stock: ")
            if not store_name.isdigit():
                store = Store.find_by_name(store_name.title())
                if store:
                    for product in products:
                        if store.id == product.store_id:
                            console.print(f"Current stock for [green bold]{product.name}[/green bold] is [magenta bold]{product.quantity}[/]\n")
                            if product.quantity > 0:
                                question = input("Enter 'u' to to update quantity for the day or 's' to stock up: ")
                            else:
                                question = input("Enter 's' to stock up: ") 
                            if question.lower() == "u":
                                if product.quantity > 0:
                                    quantity = input("Enter the number items sold today: ")
                                    if quantity.isdigit() and int(quantity) > 0:
                                        prev = product.quantity
                                        if product.quantity > int(quantity):
                                            product.quantity -= int(quantity)
                                            product.update()
                                            console.print(f"{product.name} stock has been updated from [magenta bold] {prev}[/] to [green bold]{product.quantity}[/]\n")
                                        else:
                                            console.print(f"The quantity you have entered [magenta bold] ({quantity})[/] is more then the stock [green bold]({product.quantity})[/]")
                                    else:
                                        console.print(f"\n{quantity} must be a valid integer\n", style="bold magenta")
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
                                    console.print(f"\n{quantity} must be a valid integer\n", style="bold dim magenta")
                            else:
                                console.print("\t>>>> Invalid input <<<<", style="bold dim magenta")
                        else:
                            console.print(f"\t>>>> Product {product.name} does not exist in the stock of {store.name} <<<<", style = "dim blue bold")
                else:
                    console.print(f"\t>>>> Store with name {store_name} does not exist <<<<", style = "dim blue bold")
            else:
                console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")
        else:
            console.print(f"\t>>>> Product with name {product_name} does not exist <<<<", style="dim blue bold")
    else:
        console.print(f"\t>>>> Input must be a string <<<<", style="bold dim magenta")

### QUIT ###
def quit():
    for i in track(range(2), description = "Shutting down..."):
        time.sleep(0.5)
    print(figlet_format("Retail Maven", font="small", justify="center"))
    print(figlet_format("levi", font = "italic", width=1900))
    exit()


### ADMIN PANEL ###
def store_delete_table():
    console = Console()
    console.print("Warning: This action cannot be undone!", style="yellow on red")
    ans = input("Are you sure you want to delete the store table? (y/n): ")
    if ans.lower() == "y":
        Store.drop_table()
        print("\nStore table has been deleted\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
         console.print("Invalid Input!", style="bold dim magenta")
def store_create_table():
    ans = input("Are you sure you want to create the store table? (y/n): ")
    if ans.lower() == "y":
        Store.create_table()
        print("\nStore table has been created\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
         console.print("Invalid Input!", style="bold dim magenta")
        
def department_delete_table():
    console = Console()
    console.print("Warning: This action cannot be undone!", style="yellow on red")
    ans = input("Are you sure you want to delete the department table? (y/n): ")
    if ans.lower() == "y":
        Department.drop_table()
        print("\nDepartment table has been deleted\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
        console.print("Invalid Input!", style="bold dim magenta")

def department_create_table():
    ans = input("Are you sure you want to create the department table? (y/n): ")
    if ans.lower() == "y":
        Department.create_table()
        print("\nDepartment table has been created\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
         console.print("Invalid Input!", style="bold dim magenta")

def product_delete_table():
    console = Console()
    console.print("Warning: This action cannot be undone!", style="yellow on red")
    ans = input("Are you sure you want to delete the product table? (y/n): ")
    if ans.lower() == "y":
        Product.drop_table()
        print("\nProduct table has been deleted\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
         console.print("Invalid Input!", style="bold dim magenta")
        

def product_create_table():
    ans = input("Are you sure you want to create the product table? (y/n): ")
    if ans.lower() == "y":
        Product.create_table()
        print("\nProduct table has been created\n")
    elif ans.lower() == "n":
        console.print("Operation cancelled", style="bold dim magenta")
    else:
         console.print("Invalid Input!", style="bold dim magenta")
        

