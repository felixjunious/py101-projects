import sqlite3

def print_rows(rows):
    for row in rows:
        print(row)
    print()

conn = sqlite3.connect("bank.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

print("1. List details of all customers")
rows = cursor.execute("""
        SELECT * FROM customers
    """).fetchall()
print_rows(rows)

print("2. Find all customers and their account details")
rows = cursor.execute("""
        SELECT *
        FROM customers c
        JOIN accounts a ON c.cust_id = a.cust_id
    """).fetchall()
print_rows(rows)

print("2. List all Transactions")
rows = cursor.execute("""
        SELECT *
        FROM transactions
    """).fetchall()
print_rows(rows)

conn.commit()

cursor.close()

conn.close()