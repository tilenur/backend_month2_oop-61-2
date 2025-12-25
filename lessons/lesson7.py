
import sqlite3

# A4
connect = sqlite3.connect('users.db')

# hand with pencil
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            hobby TEXT
        )
''')

connect.commit()

# CRUD - Create Read Update Delete

def create_user(name, age, hobby=None):
    # cursor.execute(
    #     f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")'
    # )

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    )

    connect.commit()
    print(f'user "{name}" created successfully')

# create_user("Ardager", 26, "fly")

# def get_users():
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     # print(users)
#     for i in users:
#         print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
#
# get_users()

def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchone()
    print(users)
    # for i in users:
    #     print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

get_users()
