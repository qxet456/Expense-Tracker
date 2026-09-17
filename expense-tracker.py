import sqlite3

sql = sqlite3.connect("expenses.db")
cursor = sql.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS Expenses (
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   Amount REAL,
   Category TEXT,
   Date TEXT Default CURRENT_DATE
   )
""")

Amount = input("Type amount : ")
Category = input("Type category : ")

cursor.execute(
    """
   INSERT INTO Expenses (Amount,Category)
   VALUES (?,?)
""",
    (Amount, Category),
)

sql.commit()
