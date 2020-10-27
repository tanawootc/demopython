import sqlite3
try:
    con=sqlite3.connect('test.db')
    con.execute('''create table product
    (proid int primary key not null,
    prodname text,
    price real
    );
    ''')
    print('create database')
except con.Error as e:
    print('error')
con.close()
