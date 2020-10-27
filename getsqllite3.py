import sqlite3
try:
    con=sqlite3.connect('test.db')
    data=con.execute('''select * from product;''')

    for row in data:
        print(row[0])
           
    print('show database')
except con.Error as e:
    if con:
        con.rollback()
    print('error')
finally:
    if con:
        con.close()
