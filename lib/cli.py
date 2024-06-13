#!usr/bin/env python
from rich import print
import time
from rich.progress import track
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt
from helpers import (
    add_new_store,
    remove_store,
    update_store,
    find_store_by_id,
    find_store_by_name,
    find_store_by_location,
    view_all_stores,
    view_all_store_departments_id,
    view_all_store_departments_name,
    new_department,
    delete_department,
    find_department_by_id,
    find_department_by_name,
    view_all_departments,
    update_department,
    new_product,
    delete_product,
    update_product,
    find_product_by_id,
    find_product_by_name,
    view_all_products,
    view_all_products_in_department_id,
    view_all_products_in_department_name,
    products_in_store_id,
    products_in_store_name,
    show_almost_out,
    update_quantity,
    store_create_table,
    store_delete_table,
    department_create_table,
    department_delete_table,
    product_create_table,
    product_delete_table,
    quit
)

def main():
    console = Console()
    for i in track(range(4), description = "Booting up..."):
        time.sleep(0.8)
    print(figlet_format("Retail Maven", font="standard",  justify="center"))
    show_almost_out()
    while True:
        choices()
        choice = Prompt.ask(f"\n>>>").lower()
        if choice == "1" or choice == "Add a new store".lower():
            add_new_store()
        elif choice == "2":
            remove_store()
        elif choice == "3":
            update_store()
        elif choice == "4":
            find_store_by_id()
        elif choice == "5":
            find_store_by_name()
        elif choice == "6":
           find_store_by_location()
        elif choice == "7":
             view_all_stores()
        elif choice == "8":
            view_all_store_departments_id()
        elif choice == "9":
            view_all_store_departments_name()
        elif choice == "10":
            new_department()
        elif choice == "11":
            delete_department()
        elif choice == "12":
            update_department()
        elif choice == "13":
            find_department_by_id()
        elif choice == "14":
            find_department_by_name()
        elif choice == "15":
            view_all_departments()
        elif choice == "16":
            new_product()
        elif choice == "17":
            delete_product()
        elif choice == "18":
            update_product()
        elif choice == "19":
            find_product_by_id()
        elif choice == "20":
            find_product_by_name()
        elif choice == "21":
            view_all_products()
        elif choice == "22":
            view_all_products_in_department_id()
        elif choice == "23":
            view_all_products_in_department_name()
        elif choice == "24":
            products_in_store_id()
        elif choice == "25":
            products_in_store_name()
        elif choice == "26":
            update_quantity()
        elif choice == "q".lower() or choice == "quit".lower():
            quit()
        elif choice.lower() == "admin":
            pass_ = input("Enter admin password: ")
            if pass_ == "admin":
                admin_panel()
            else:
                console.print("Invalid Password!", style="bold dim magenta")
        else:
            console.print("Invalid Input!", style="bold dim magenta")
        
        
def choices():
    console = Console()
    console.print("\nStore Operations:", style = "bold blue on white")
    print(f"\t1. Add new store")
    print(f"\t2. Remove store")
    print(f"\t3. Update store details")
    print(f"\t4. Find store by id")
    print(f"\t5. Find store by name")
    print(f"\t6. Find stores in a location")
    print(f"\t7. View all stores")
    print(f"\t8. View all departments in a store (by ID)")
    print(f"\t9. View all departments in a store (by Name)")
    console.print("\nDepartment Operations:", style = "bold blue on white")
    print(f"\t10. Add new department")
    print(f"\t11. Remove department")
    print(f"\t12. Update department details")
    print(f"\t13. Find department by id")
    print(f"\t14. Find department(s) by name")
    print(f"\t15. View all departments")
    console.print("\nProduct Operations:", style = "bold blue on white")
    print(f"\t16. Add new product")
    print(f"\t17. Remove product")
    print(f"\t18. Update product details")
    print(f"\t19. Find product by id")
    print(f"\t20. Find product(s) by name")
    print(f"\t21. View all products")
    print(f"\t22. View all products in a department (by ID)")
    print(f"\t23. View all products in a department (by Name)")
    print(f"\t24. View all products in a store (by ID)")
    print(f"\t25. View all products in a store (by Name)")
    print(f"\t26. Update product quantity")
    print(f"\nEnter 'q' or 'quit' to Quit")
    
    
def admin_panel():
    flag = True
    while flag:
        admin_choices()
        choice = input(">>  ")
        if choice.lower() == "1":
            store_delete_table()
        elif choice.lower() == "2":
            store_create_table()
        elif choice.lower() == "3":
            department_delete_table()
        elif choice.lower() == "4":
            department_create_table()
        elif choice.lower() == "5":
            product_delete_table()
        elif choice.lower() == "6":
            product_create_table()
        elif choice.lower() == "q" or choice.lower() == "quit":
            flag = False
            main()
        else:
            print("Invalid input")
            
            
def admin_choices():
    console = Console()
    console.print("\n!!!!Admin panel!!!!!", style = "bold underline red")
    console.print("Store Operations", style = "bold blue on white")
    print("\t1. Delete Store Table")
    print("\t2. Add Store Table")
    console.print("Department Operations", style = "bold blue on white")
    print("\t3. Delete Department Table")
    print("\t4. Add Department Table")
    console.print("Product Operations", style = "bold blue on white")
    print("\t5. Delete Product Table")
    print("\t6. Add Product Table")
    print(f"\nEnter 'q' or 'quit' to go back")

if __name__ == "__main__":
    main()