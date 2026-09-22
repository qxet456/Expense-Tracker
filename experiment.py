import sqlite3

sql = sqlite3.connect("EXpenses.db")
cursor = sql.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS Expenses (
   ID INTEGER PRIMARY KEY AUTOINCREMENT,                             
   Amount REAL,                                                                                  
   Category TEXT,
   Date TEXT Default CURRENT_DATE
   )
""")


def add_expense():
    while True:
        Amount = input("Type amount : ")
        try:
            amount = float(Amount)
            break
        except ValueError:
            print("Type an amount !")

    Category = input("Type category : ")

    cursor.execute(
        """
       INSERT INTO Expenses (Amount,Category)
       VALUES (?,?)
    """,
        (amount, Category),
    )

    sql.commit()


def view_expenses():
    cursor.execute("""
    SELECT * FROM Expenses
    """)
    x = cursor.fetchall()
    for i in x:
        print(i)

    sql.commit()


def delete_expense():
    view_expenses()
    while True:
        ask_id = input("Type an ID : ")
        try:
            z = int(ask_id)
            cursor.execute(
                """
            DELETE FROM Expenses 
            WHERE ID = ?
            """,
                (z,),
            )
            sql.commit()
            break
        except ValueError:
            print(ask_id, "is not an ID !")

def update_expense():
    while True:
        view_expenses()
        Ask_id = input("Type an ID : ")
        try:
            y = int(Ask_id)
            cursor.execute("""
            SELECT * FROM Expenses WHERE ID = ?
            """,(y,),
            )

            p = cursor.fetchone()
            
            if p == None:
                print("ID not valid !")
            else:
                print(p)

            sql.commit()
            break
        except ValueError:
            print(Ask_id , "is not an ID !")


while True:
    print("---------Expense-Tracker----------")
    print("<===================================>")
    print("--- OPTIONS ---")
    print("-------------------------------------")
    print("A. ADD EXPENSE")
    print("B. VIEW EXPENSES")
    print("C. DELETE EXPENSE")
    print("D. UPDATE EXPENSE")
    print("E. EXIT")
    print("-------------------------------------")
    print("<===================================>")
    choice = input("Type your choice : ")
    if choice == "A" or choice == "a":
        add_expense()
    elif choice == "B" or choice == "b":
        view_expenses()
    elif choice == "C" or choice == "c":
        delete_expense()
    elif choice == "D" or choice == "d":
        update_expense()
    elif choice == "E" or choice == "e":
        break
    else:
        print(choice, "is not an option !")
