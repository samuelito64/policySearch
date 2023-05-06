import os
import sqlite3

def create_database():
    database_file = './networksPolicies/networks.db'
    if os.path.isfile(database_file):
        print("The database already exists.")
    else:
        conn = sqlite3.connect(database_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE networks
                  (id INTEGER PRIMARY KEY, ipAddress TEXT, network TEXT, policy TEXT, domain TEXT)''')
        conn.commit()
        conn.close()
        print("Database has been created successfully.")
