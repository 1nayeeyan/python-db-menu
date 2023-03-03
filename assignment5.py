import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3309,
    user="newuser",
    database="soccer"
) # change the above paramaters to match required database 

mycursor = db.cursor()

# define menu options
menu_options = {
    "1": "Drop Table",
    "2": "Create Table",
    "3": "Populate Table",
    "4": "Query Tables",
    "5": "Join Tables",
    "6": "Display Tables",
    "7": "Exit"
}

# display menu options
def display_menu():
    print("Main Menu - Select Desired Operation(s): \n")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    print("")

# execute menu choice
def execute_choice(choice):
    if choice == "1":
        drop_table()
    elif choice == "2":
        create_table()
    elif choice == "3":
        populate_table()
    elif choice == "4":
        query_tables()
    elif choice == "5":
        join_tables()
    elif choice == "6":
        display_tables()
    elif choice == "7":
        print("Exiting program...")
        exit()
    else:
        print("Invalid choice. Please try again.")
    print("")

# drop table
def drop_table():
    table_name = input("Enter the name of the table to drop: ")
    sql = f"DROP TABLE IF EXISTS {table_name}"
    mycursor.execute(sql)
    print('\n')
    print(f"{table_name} table dropped successfully.")

# create table
def create_table():
    table_name = input("Enter the name of the table to create: ")
    sql = input("Enter the CREATE TABLE statement: ")
    mycursor.execute(sql)
    print('\n')
    print(f"{table_name} table created successfully.")

# populate table
def populate_table():
    table_name = input("Enter the name of the table to populate: ")
    values = input("Enter the INSERT statement: ")
    mycursor.execute(values)
    db.commit()
    print('\n')
    print(f"{table_name} table populated successfully.")

# query tables
def query_tables():
    table_name = input("Enter the headers of the table to query: ")
    sql = input("Enter the SELECT statement: ")
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('\n')
    print(table_name)
    print('\n')
    for row in result:
        print(row)


# join tables
def join_tables():
    table1 = input("Enter the first table name: ")
    table2 = input("Enter the second table name: ")
    on = input("Enter the ON statement: ")
    sql = f"SELECT * FROM {table1} INNER JOIN {table2} ON {on}"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('\n')
    for row in result:
        print(row)

# display table
def display_tables():
    table_name = input("Enter the name of the table to display: ")
    sql = input("To query the table, enter 'DESCRIBE tble_name' excluding the ticks: ")
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print('\n')
    for row in result:
        print(row)

# main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    execute_choice(choice)