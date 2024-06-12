#!usr/bin/env python
import time
from helpers import (
    add_new_store,
    remove_store,
    update_store,
    find_store_by_id,
    find_store_by_name,
    find_store_by_location,
    view_all_stores,
    view_all_store_departments,
    new_department,
    delete_department,
    find_department_by_id,
    find_department_by_name,
    view_all_departments,
    update_department,
    quit
)

def main():
    # for frame in '|/-\\|/-\\|/-\\|':
    #     print(f'\r{frame}', end='', flush=True)
    #     time.sleep(0.2)
    st = "*" * (len("Welcome to the store manager!") + 6)
    print(f"\n\t{st}")
    print(f"\t **Welcome to the store manager!**")
    print(f"\t{st}")
    while True:
        choices()
        choice = input(f"\n>>>  ")
        if choice == "1" or choice == "Add a new store".lower():
            add_new_store()
        elif choice == "2":
            remove_store()
        elif choice == "3":
            update_store()
        elif choice == "4":
            find_store_by_id
        elif choice == "5":
            find_store_by_name()
        elif choice == "6":
           find_store_by_location()
        elif choice == "7":
             view_all_stores()
        elif choice == "8":
            view_all_store_departments()
        elif choice == "9":
            new_department()
        elif choice == "10":
            delete_department()
        elif choice == "11":
            update_department()
        elif choice == "12":
            find_department_by_id()
        elif choice == "13":
            find_department_by_name()
        elif choice == "14":
            view_all_departments()
        elif choice == "q".lower() or choice == "quit".lower():
            quit()
        else:
            print("Invalid choice")
        
        
def choices():
    print("Store Operations:")
    print(f"\t1. Add new store")
    print(f"\t2. Remove store")
    print(f"\t3. Update store details")
    print(f"\t4. Find store by id")
    print(f"\t5. Find store by name")
    print(f"\t6. Find stores in a location")
    print(f"\t7. View all stores")
    print(f"\t8. View all departments in a store")
    print("\nDepartment Operations:")
    print(f"\t9. Add new department")
    print(f"\t10. Remove department")
    print(f"\t11. Update department details")
    print(f"\t12. Find department by id")
    print(f"\t13. Find department(s) by name")
    print(f"\t14. View all departments")
    print(f"\nEnter 'q' or 'quit' to Quit")
    
if __name__ == "__main__":
    main()