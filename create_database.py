import sqlite3
import random
import datetime

#creating tables

create_sales_table = '''CREATE TABLE sales (
                        sale_id INTEGER PRIMARY KEY,
                        sale_date DATE,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10,2),
                        total_price DECIMAL(10,2),
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES products(product_id)
                    )'''

create_customers_table = '''CREATE TABLE customers (
                            customer_id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            phone TEXT
                        )'''

create_products_table = '''CREATE TABLE products (
                            product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            unit_cost DECIMAL(10,2)
                        )'''

#inserting data into the tables

insert_products_data = '''INSERT INTO products (product_name, unit_cost) VALUES (?,?)'''

insert_sales_data = '''INSERT INTO sales (sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES (?,?,?,?,?,?)'''

insert_customers_data = '''INSERT INTO customers (first_name, last_name, email, phone) VALUES (?,?,?,?)'''

#define data for the products and customers tables

products = [('Dress', 50.00),('Jacket', 120.00),('T-shirt', 30.00),('Belt', 40.00),('Trousers', 60.00)]

customers = [('Aria','Montgomery','armont@example.com','555-2134'),
             ('Hanna','Marin','hanmar@example.com','555-1243'),
             ('Spencer','Hastings','spenhast@example.com','555-7352'),
             ('Emily','Fields','emfield@example.com','555-9257'),
             ('Alison','DiLaurentis','alldis@example.com','555-5364'),
             ('Ezra','Fitz','ezfit@example.com','555-8364'),
             ('Jenna','Marshall','jenmar@example.com','555-7369'),
             ('Mona','Vanderwall','monvand@example.com','555-3856'),
             ('Caleb','Rivers','calri@example.com','555-2438'),
             ('Toby','Cavanaugh','tobcav@example.com','555-2635'),
             ('Maya','St. Germain','mayger@example.com','555-7453'),
             ('Wren','Kingston','wrekin@example.com','555-8473'),
             ('Charlotte','DiLaurentis','cecedrake@example.com','555-5243')
]

#define the start and end dates for generating sales data
start_date = datetime.date(2023,1,1)
end_date = datetime.date(2023,12,31)

#connect to the database and create the tables
with sqlite3.connect('sales.db') as conn:

    conn.execute(create_sales_table)            #create tables
    conn.execute(create_products_table)
    conn.execute(create_customers_table)

    for product in products:                                #insert data into tables
        conn.execute(insert_products_data, product)
    for customer in customers:
        conn.execute(insert_customers_data, customer)
    for i in range(1000):
        sale_date = start_date + datetime.timedelta(days=random.randint(0,364))
        customer_id = random.randint(1, len(customers))
        product_id = random.randint(1, len(products))
        quantity = random.randint(1,10)
        unit_price = products[product_id-1][1]
        total_price = quantity * unit_price
        conn.execute(insert_sales_data, (sale_date,customer_id,product_id,quantity,unit_price,total_price))

    #commit the changes
    conn.commit()

    print("Database successfully created")