# Expense Tracker (Python CLI Application) 

# Description
A command-Line based expense traccker built using Python.
The Application allows user to record income and expenses,
view transactions history, generate summaries and export 
reports using a clean and modular code structure.

# Features
- Add income and expense transactions.
- View all transactions in a tabular format.
- Delete transactions by index.
- View Financial Summary (Total income, expense, balance).
- View Category-wise expense summary.
- Export transactions reports to CSV and TXT.
- Persistent data storage using CSV files.

# Project Structure

Expense tracker/
|
|__ src/
|    |__main.py            --  #Entry point and menu handling    
|    |__storage.py         --  #CSV storage and data persistence logic
|    |__utilities.py       --  #Helper functions
|    |__reports/           --  #Exported Reports
|
|__ data/
|    |__transaction.csv    --  #Transactions storage
|
|__ README.md
|
|__ .gitignore

# Technologies used

- Python
- CSV module
- Logging module
- Git & GitHub

# How to Run

1. Clone the repository: 
   git clone 
2. Navigate to the project directory: 
   cd Expense tracker/src
3. Run the application:
   python main.py

# Learning Outcomes

- Structuring a Python project using multiple modules
- File handling and persistent storage using CSV
- Implement menu-driven CLI application
- Debugging real-world issues related to file paths and data consistency
- Using Git and GitHub for version control

# Author
Ankita Thakur
1st Year, B.Tech CSE  