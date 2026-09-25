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
    expenses = cursor.fetchall()

    print(
        "<===========================================================================================================>"
    )
    print(f"{'ID':<5} {'AMOUNT':<12} {'CATEGORY':<22} {'DATE':<12}")
    print(
        "<===========================================================================================================>"
    )

    for expense in expenses:
        id, amount, category, date = expense

        print(f"{id:<5} ₹{amount:<11.2f} {category:<22} {date:<12}")

    print(
        "<===========================================================================================================>"
    )

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
        ask_id = input("Type an ID : ")
        try:
            y = int(ask_id)
            cursor.execute(
                """
            SELECT * FROM Expenses WHERE ID = ?
            """,
                (y,),
            )

            p = cursor.fetchone()

            if p is None:
                print("ID not valid !")
            else:
                print("----- OPTIONS -----")
                print("<==================>")
                print("A. Amount")
                print("B. Category")
                print("C. Date")
                print("<===================>")
                ask_choice = input("Type your choice : ")
                if ask_choice == "A" or ask_choice == "a":
                    new_amount = input("Type the new amount : ")
                    cursor.execute(
                        """
                    UPDATE Expenses
                    SET Amount = ?
                    WHERE ID = ? 
                    """,
                        (new_amount, y),
                    )
                elif ask_choice == "B" or ask_choice == "b":
                    new_category = input("Type the new category :")
                    cursor.execute(
                        """
                    UPDATE Expenses
                    SET Category = ? 
                    WHERE ID = ?
                    """,
                        (new_category, y),
                    )
                elif ask_choice == "C" or ask_choice == "c":
                    new_date = input("Type the new date : ")
                    cursor.execute(
                        """
                    UPDATE Expenses
                    SET Date = ?
                    WHERE ID = ?
                    """,
                        (new_date, y),
                    )
                else:
                    print(ask_choice, "is not an option !")
            sql.commit()
            break
        except ValueError:
            print(ask_id, "is not an ID !")


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
