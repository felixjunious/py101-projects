import sqlite3

conn = sqlite3.connect("bank.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        cust_id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        email TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        acc_id INTEGER PRIMARY KEY,
        cust_id INTEGER,
        acc_type TEXT,
        balance REAL,
        FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        trans_id INTEGER PRIMARY KEY,
        acc_id INTEGER,
        trans_type TEXT,
        amount REAL,
        date DATE,
        FOREIGN KEY (acc_id) REFERENCES accounts(acc_id)
    );
""")

conn.commit()

cursor.close()

conn.close()