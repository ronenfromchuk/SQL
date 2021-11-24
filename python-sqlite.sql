import sqlite3

con = sqlite3.connect('C:/itay/sqlite/mydb2.db')
cur = con.cursor()

cur.execute("select * from shopping")

for row in enumerate(cur):
    print(row)

def add_item(cur, table, id, name, amount, maavar):
    cur.execute(f'INSERT INTO {table} VALUES ({id}, "{name}",'\
                f' {amount}, {maavar})')

#cur.execute("INSERT INTO shopping VALUES (8, 'humus', 12, 7)")
add_item(cur, "shopping", 8, 'humus', 12, 7)

cur.execute("UPDATE shopping SET amount=14"\
            " WHERE name = 'humus'")

cur.execute("DELETE FROM shopping "\
            " WHERE name = 'humus'")

con.commit();

con.close()
