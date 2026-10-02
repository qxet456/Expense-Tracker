# 💰 CLI Expense Tracker

A simple command-line expense tracker built with **Python** and **SQLite**.

This project allows users to add, view, update, delete, and filter expenses directly from the terminal. Expense data is stored locally in an SQLite database so it can be accessed between sessions.

## ✨ Features

- ➕ Add new expenses
- 📋 View all expenses
- ✏️ Update existing expenses
  - Amount
  - Category
  - Date
- 🗑️ Delete expenses by ID
- 🔎 Filter expenses by:
  - Category
  - Date
  - Amount
- 📅 Automatically stores the current date when an expense is added
- ✅ Input validation for amounts, IDs, and dates
- 💾 Local data storage using SQLite

## 🛠️ Technologies Used

- Python
- SQLite
- Python `sqlite3` module
- Python `datetime` module

## 📁 Project Structure

```text
Expense-Tracker/
│
├── expense-tracker.py
├── Expenses.db
├── README.md
└── .gitignore