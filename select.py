import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database Successfully")

cursor = conn. execute("SELECT ID, NAME, AGE, SALARY FROM EMPLOYEES4")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])

print("Records found")
conn.close()