import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO customers (cust_id, name, address, email)
    VALUES
        (110, 'Anil', 'Mumbai', 'anil@gmail.com'),
        (111, 'Smith', 'Delhi', 'smith@example.com'),
        (112, 'Ramesh', 'Mumbai', 'ramesh@gmail.com'),
        (113, 'Khan', 'Delhi', 'khan@example.com');
""")

cursor.execute("""
    INSERT INTO accounts (acc_id, cust_id, acc_type, balance)
    VALUES
        (101, 110, 'Savings', 2500.0),
        (102, 111, 'Checking', 1200.5),
        (103, 112, 'Savings', 1500.0),
        (104, 113, 'Checking', 1700.0);
""")

cursor.execute("""
    INSERT INTO transactions (trans_id, acc_id, trans_type, amount, date)
    VALUES
        (1, 101, 'deposit', 500.0, '2025-07-04'),
        (2, 102, 'withdrawal', 100.0, '2025-07-05'),
        (3, 103, 'deposit', 300.0, '2025-07-08'),
        (4, 104, 'withdrawal', 200.0, '2025-07-09'),
        (5, 102, 'deposit', 500.0, '2025-08-11'),
        (6, 103, 'withdrawal', 100.0, '2025-08-22'),
        (7, 104, 'deposit', 500.0, '2025-09-01'),
        (8, 104, 'withdrawal', 100.0, '2025-09-10');
""")

conn.commit()

cursor.close()

conn.close()