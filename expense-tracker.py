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

while True:
    Amount = input("Type Amount : ")
    try:
        Amount = float(Amount)
        break
    except ValueError:
        print("Type an amount !")

Category = input("Type category :")

cursor.execute(
    """
   INSERT INTO Expenses (Amount,Category)
   VALUES (?,?)                                
""",
    (Amount, Category),
)

sql.commit()
