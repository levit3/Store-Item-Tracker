#!usr/bin/env python
import time
from helpers import (
    add_new_store,
    remove_store,
    update_store,
    find_by_id,
    find_by_name,
    find_by_location,
    view_all,
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
            find_by_id()
        elif choice == "5":
            find_by_name()
        elif choice == "6":
            find_by_location()
        elif choice == "7":
            view_all()
        elif choice == "8" or choice == "q".lower() or choice == "quit".lower():
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
    print(f"\t8. Quit")
    
if __name__ == "__main__":
    main()