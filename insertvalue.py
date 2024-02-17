import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database Successfully")

conn.execute("INSERT INTO EMPLOYEES4 VALUES (20,'FAITH KARIMI',34,450000.00)")
conn.execute("INSERT INTO EMPLOYEES4 VALUES (21,'Jane KARIMI',51,800000.00)")
conn.execute("INSERT INTO EMPLOYEES4 VALUES (22,'Haan KARIMI',64,1200000.00)")
conn.execute("INSERT INTO EMPLOYEES4 VALUES (24,'Heooo KARIMI',29,350000.00)")
conn.execute("INSERT INTO EMPLOYEES4 VALUES (25,'Kim KARIMI',18,300000.00)")

conn.commit()
print("Records inserted succesfully")
conn.close()