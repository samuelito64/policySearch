import sqlite3
from database import create_database
from tabulate import tabulate

def search(query):
    db_name = "./networksPolicies/networks.db"
    try:
        #db connection
        conn= sqlite3.connect(db_name)
        cursor= conn.cursor()
        # run query
        cursor.execute(query)
        result = cursor.fetchall()
        # Print Resu
        print(tabulate(result, headers=["IPAddress","Network","Policy","Domain"],tablefmt="fancy_grid"))
        # Close Connection
        conn.close()
    except sqlite3.Error as error:
        print("error conecting to the data base",error)
def addIP():
    pass
    # Código para agregar un nuevo registro

def modify():
    pass
    # Código para modificar un registro existente

def delete():
    pass
    # Código para borrar un registro existente

def main():
    create_database()

    # Conexión a la base de datos
    conn = sqlite3.connect('networks.db')
    c = conn.cursor()

    # Menú principal
    while True:
        print("##################################")
        print("#        Choise an option:       #")
        print("#            1. Search           #")
        print("#            2. AddIP            #")
        print("#            3. Modify           #")
        print("#            4. Delete           #")
        print("#            5. Exit             #")
        print("##################################")

        opcion = input("Choose an option and enter the number: ")

        if opcion == "1":
            query = input("input IP o network: ")
            query = "select * from networks where ipAddress like '%" + query + "%'"
            search(query)
        elif opcion == "2":
            addIP()
        elif opcion == "3":
            modify()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Exit!")
            break
        else:
            print("Invalid option. Please enter an option from 1 to 5.")

    # Cierre de conexión
    conn.close()

if __name__ == "__main__":
    main()
