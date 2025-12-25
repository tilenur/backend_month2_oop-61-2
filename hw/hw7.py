import sqlite3

# A4
connect = sqlite3.connect("products.db")
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            title VARCHAR(50) NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
""")
connect.commit()

# CRUD - Create Read Update Delete + get_by_rowid

def create_product(title, price, quantity):
    cursor.execute(
        "INSERT INTO products(title, price, quantity) VALUES(?,?,?)",
        (title, price, quantity)
    )
    connect.commit()
    print(f'товар добавлен {title}!!')

# create_product("iPhone case", 1500, 3)


def get_products():
    cursor.execute("SELECT rowid, title, price, quantity FROM products")
    products = cursor.fetchall()

    for i in products:
        print(f"ROWID: {i[0]} TITLE: {i[1]} PRICE: {i[2]} QTY: {i[3]}")

# get_products()


def get_by_rowid(row_id):
    cursor.execute(
        "SELECT rowid, title, price, quantity FROM products WHERE rowid = ?",
        (row_id,)
    )
    product = cursor.fetchone()

    if product:
        print(f"ROWID: {product[0]} TITLE: {product[1]} PRICE: {product[2]} QTY: {product[3]}")
    else:
        print("такого rowid нет!!")

# get_by_rowid(1)


def update_product(row_id, title, price, quantity):
    cursor.execute(
        "UPDATE products SET title = ?, price = ?, quantity = ? WHERE rowid = ?",
        (title, price, quantity, row_id)
    )
    connect.commit()
    print("товар обновлен!")

# update_product(1, "iPhone case black", 1700, 5)


def delete_product(row_id):
    cursor.execute(
        "DELETE FROM products WHERE rowid = ?",
        (row_id,)
    )
    connect.commit()
    print("товар удален!!")

# delete_product(2)



create_product("iPhone case", 1500, 3)
create_product("USB-C cable", 800, 10)
create_product("Keyboard", 4500, 2)