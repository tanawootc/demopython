import sqlite3
try:
    con=sqlite3.connect('test.db')
    con.execute('''insert into product
    (proid,prodname,price)
    values(3,'iphone',100);
    ''')
    con.execute('''insert into product
    (proid,prodname,price)
    values(4,'iphone',100);
    ''')
    print('save database')
except con.Error as e:
    if con:
        con.rollback()
    print('error')
finally:
    if con:
        con.close()
