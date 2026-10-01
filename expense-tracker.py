import sqlite3
from datetime import date

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


def display_expenses(expenses):
    print("<=================================================================>")
    print(f"{'ID':<5} {'AMOUNT':<12} {'CATEGORY':<22} {'DATE':<12}")
    print("<=================================================================>")

    for expense in expenses:
        id, amount, category, date = expense
        print(f"{id:<5} ₹{amount:<11.2f} {category:<22} {date:<12}")

    print("<=================================================================>")


def add_expense():
    while True:
        amount = input("Type amount : ")
        try:
            real_amount = float(amount)
            break
        except ValueError:
            print("Type an amount !")

    category = input("Type category : ")

    cursor.execute(
        """
       INSERT INTO Expenses (Amount,Category)
       VALUES (?,?)
    """,
        (real_amount, category),
    )

    sql.commit()


def view_expenses():
    cursor.execute("""
    SELECT * FROM Expenses
    """)
    expenses = cursor.fetchall()

    print("<=================================================================>")
    print(f"{'ID':<5} {'AMOUNT':<12} {'CATEGORY':<22} {'DATE':<12}")
    print("<=================================================================>")

    for expense in expenses:
        id, amount, category, date = expense
        print(f"{id:<5} ₹{amount:<11.2f} {category:<22} {date:<12}")

    print("<=================================================================>")


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
            p = cursor.fetchone()

            if p == [] or p is None:
                print("ID not valid !")
            sql.commit()
            break
        except ValueError:
            print(ask_id, " is not an ID !")


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


def search_expense():
    while True:
        print("---------- FILTER/SORT OPTIONS --------------")
        print("<===========================================>")
        print("A. Category")
        print("B. Date")
        print("C. Amount")
        print("D. Back")
        print("<===========================================>")
        ask_choice = input("Type your choice : ")
        if ask_choice == "A" or ask_choice == "a":
            ask_category = input("Type your category : ")
            cursor.execute("""
            SELECT * FROM Expenses WHERE Category = ?
            """,
            (ask_category,),)
            results = cursor.fetchall()
            if results is None or results == []:
                print("INVALID CATEGORY !")
            else:
                display_expenses(results)
        elif ask_choice == "B" or ask_choice == "b":
            ask_date = input("Type your date : ")
            try:
                date.fromisoformat(ask_date)
                cursor.execute("""
                SELECT * FROM Expenses WHERE Date = ?
                """,
                (ask_date,),)
                results = cursor.fetchall()
                if results is None or results == []:
                    print("INVALID DATE")
                else:
                    display_expenses(results)
            except ValueError:
                print("USE YYYY-MM-DD FORMAT")
        elif ask_choice == "C" or ask_choice == "c":
            ask_amount = input("Type the amount : ")
            try:
                new_amount = float(ask_amount)
                cursor.execute("""
                SELECT * FROM Expenses WHERE Amount = ?
                """,
                (new_amount,),)
                results = cursor.fetchall()
                if results is None or results == []:
                    print("INVALID AMOUNT")
                else:
                    display_expenses(results)
            except ValueError:
                print("Type a number!")
        elif ask_choice == "D" or ask_choice == "d":
            break
        else:
            print(ask_choice , "is not an option !")


while True:
    print("---------Expense-Tracker----------")
    print("<===================================>")
    print("--- OPTIONS ---")
    print("-------------------------------------")
    print("A. ADD EXPENSE")
    print("B. VIEW EXPENSES")
    print("C. DELETE EXPENSE")
    print("D. UPDATE EXPENSE")
    print("E. FILTER/SORT EXPENSE")
    print("F. EXIT")
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
        search_expense()
    elif choice == "F" or choice == "f":
        break
    else:
        print(choice, "is not an option !")
