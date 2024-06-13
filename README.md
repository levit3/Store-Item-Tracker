# Store Inventory Management Ststem

This application manages stock across multiple stores and departments, utilizing Object Relational Mapping (ORM) for seamless database interaction. 
Users can perform CRUD operations on departments, stores, and products using a Command-Line Interface (CLI).
The application creates a user friendly way to view products together with the stock and the various departments across multiple stores in an easy and quick way.


## Key Features
- The user is able to add, update and delete the attributes in a table (store, department, product).
- The user is able to update the stock of items in different stores.
- The user is able to view all items in a particular table.
- The admin is able to create and delete various tables.

## Usage
1. Clone the repository
2. Install the dependencies using `pipenv install`
3. Enter the environment using `pipenv shell`
4. Run `python3 -m lib.db.seed` to reset the tables.
5. Run `python3 lib/cli.py` to run the application.

## Installation Requirements
- Pip
- Python

## Technologies Used
- Python
- Rich (Library)
- Pyfiglet (Library)

## Support and Contact Details
For any inquiries email me at lvmwendwa4@gmail.com


