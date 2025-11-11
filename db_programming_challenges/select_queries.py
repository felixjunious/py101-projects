import sqlite3

conn = sqlite3.connect("univ.db")

cursor = conn.cursor()

print("1. All the cities where Students are living")
rows = cursor.execute("SELECT DISTINCT city FROM students").fetchall()
for row in rows:
    print(row[0], end=' ')
print('\n')

print("2. Student Names from 'CSE' Department")
rows = cursor.execute("""
        SELECT name 
        FROM students s
        JOIN dept d ON s.deptno = d.deptno
        WHERE d.dname = 'CSE'
    """).fetchall()
for row in rows:
    print(row[0], end=' ')
print('\n')

print("3. 'Civil' Department Students not from 'MUM'")
rows = cursor.execute("""
        SELECT s.name
        FROM students s
        JOIN dept d ON s.deptno = d.deptno
        WHERE d.dname = 'Civil' AND s.city <> 'MUM'
    """).fetchall()
for row in rows:
    print(row[0], end=' ')
print('\n')

print("4. Number of 'ECE' Students residing in each city")
rows = cursor.execute("""
        SELECT city, count(*)
        FROM students s
        JOIN dept d ON s.deptno = d.deptno
        WHERE d.dname = 'ECE'
        GROUP BY s.city
    """).fetchall()
for row in rows:
    print(row[0], row[1])
print('\n')

print("5. Departments having strength more than strength of 'ECE' Department")
rows = cursor.execute("""
        SELECT d.dname, count(*)
        FROM students s
        JOIN dept d ON s.deptno = d.deptno
        GROUP BY d.deptno
        HAVING count(*) >
            (SELECT count(*)
            FROM students s
            JOIN dept d ON s.deptno = d.deptno
            WHERE d.dname = 'ECE')
    """).fetchall()
for row in rows:
    print(row[0], row[1])
print('\n')

conn.commit()

cursor.close()

conn.close()
