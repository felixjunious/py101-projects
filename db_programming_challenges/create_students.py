import sqlite3

data = [
    (1, "Smith", "NY", 10),
    (2, "John", "CA", 10),
    (3, "Ajay", "DL", 20),
    (4, "Smith", "WA", 20),
    (5, "Khan", "MUM", 30),
    (6, "Alex", "CA", 30),
    (7, "Katrina", "NY", 30),
    (8, "Pevan", "MUM", 30),
    (9, "Kiran", "PAR", 10),
    (10, "William", "NY", 10),
    (11, "Roger", "CA", 40),
    (12, "Hannah", "PAR", 20),
    (13, "Anthony", "WA", 20),
    (14, "Keerthi", "MUM", 40),
    (15, "Suman", "DL", 10)
]

with sqlite3.connect("univ.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT,
            deptno INTEGER,
            FOREIGN KEY (deptno) REFERENCES dept(deptno)
        );
    """)

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.executemany(
        "INSERT INTO students(roll, name, city, deptno) VALUES (?, ?, ?, ?)",
        data
    )
