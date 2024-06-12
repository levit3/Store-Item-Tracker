from models.store import Store
from models.department import Department
from models.product import Product

def add_new_store():
    name = input("Enter the name of the new store: ")
    location = input("Enter the location of the new store: ")
    Store.create(name, location)

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
            location = input("Enter the new store location: ")
            store.name = name
            store.location = location
            store.update()
        except Exception as exc:
            print(f"\t>>>> Error: ", exc, "<<<<", "\n")
    elif id_:
        print(f"\t>>>> No store with id {id_} was found <<<<")
    else:
        print(f"\t>>>> Input cannot be blank <<<<")
        
def find_by_id():
    id_ = input("Enter the store id:  ")
    store = Store.find_by_id(id_)
    if store:
        print(f"\n{store}\n")
    else:
        print(f"\t>>>> Store with id {id_} not found <<<<")

def find_by_name():
    name = input("Enter the store name:  ")
    store = Store.find_by_name(name)
    if store:
        print(f"\n{store}\n")
    else:
        print(f"\t>>>> Store with the name {name} not found <<<<")

def find_by_location():
    location = input("Enter the location:  ")
    stores = Store.find_in_location(location.title())
    if stores:
        for store in stores:
            print(f"{store}")
    else:
        print(f"\t>>>> No stores found in {location} <<<<")

def view_all():
    stores = Store.get_all()
    for store in stores:
        print(store)


def quit():
    st = "*" * (len("Store manager") + 6)
    print(f"\t      {st}")
    print(f"\t       **Store manager**")
    print(f"\t      {st}")
    exit()
