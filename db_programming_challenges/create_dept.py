import sqlite3

data = [
    (10, "CSE"),
    (20, "ECE"),
    (30, "Civil"),
    (40, "Mech.")
]

with sqlite3.connect("univ.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dept(
            deptno INTEGER PRIMARY KEY,
            dname TEXT
        );
    """)

    cursor.executemany(
        "INSERT INTO dept(deptno, dname) VALUES (?, ?)",
        data
    )
