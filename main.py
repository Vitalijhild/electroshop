import sqlite3

conn  = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
);

''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
               customer_id INTEGER PRIMARY KEY,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE );
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL, 
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id) );
               ''')

while True:
    ans =  int(input("1- add product; 2 - add customer; 3 - new order: "))
    if ans == 1:
        product_name = input('Enter name: ')
        product_category = input('Enter category: ')
        product_price = input('Enter price: ')
        query = '''
                INSERT INTO products(
                name,
                category,
                price
                )
                VALUES(?,?,?)
                '''
        cursor.execute(query,[product_name, product_category,float(product_price)])
        conn.commit()
    if ans == 2:
        first_name = input('Enter name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email: ')
        query = '''
                INSERT INTO customers(
                first_name,
                last_name,
                email
                )
                VALUES(?,?,?)
                '''
        cursor.execute(query,[first_name, last_name, email])
        conn.commit()

    if ans == 3:
        customer_id = input('Enter customer id: ')
        product_id = input('Enter product id: ')
        quantity = input('Enter quantity: ')
        order_date = input('Enter order date: ')
        query = '''
                INSERT INTO orders(
                customer_id,
                product_id,
                quantity,
                order_date
                )
                VALUES(?,?,?,?)
                '''
        cursor.execute(query,[customer_id, product_id, quantity, order_date])
        conn.commit()
    else:
        break