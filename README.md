# project6
This is a menu-driven Journal Manager program that allows users to add, view, search, and delete journal entries stored in a file. It uses file handling, exception handling, and date-time features to manage personal journal data efficiently.


# 📔 Journal Manager

A simple **Python-based Journal Management System** that allows users to create, view, search, and delete journal entries through a menu-driven console interface.

The project demonstrates important Python concepts such as **Object-Oriented Programming (OOP), File Handling, Exception Handling, Date & Time, Classes, Methods, Loops, Conditional Statements, and User Input**.

---

## 📌 Project Overview

The **Journal Manager** is a console-based application designed to store personal journal entries inside a text file.

Each journal entry is automatically saved with the **current date and time**, making it easy to maintain a chronological record.

The application provides four main operations:

* ➕ Add New Journal Entry
* 📖 View All Journal Entries
* 🔎 Search Journal Entries
* 🗑️ Delete All Journal Entries

A menu-driven system allows the user to continuously perform these operations until choosing **Exit**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Learn Python file handling
* Understand Object-Oriented Programming
* Store data permanently in a text file
* Add timestamps to records
* Read stored records
* Search data using keywords or dates
* Delete stored data safely with confirmation
* Handle common file-related errors
* Build a menu-driven Python application
* Practice exception handling using `try-except`

---

## 🛠️ Technologies Used

* **Python 3**
* `os` module
* `datetime` module
* File Handling
* Object-Oriented Programming
* Exception Handling

---

## 📂 Project Structure

```text
Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

> `journal.txt` is created automatically when the first journal entry is added.

---

# 🧠 Python Concepts Used

## 1. Object-Oriented Programming

The project uses a class named:

```python
class JournalManager:
```

The class contains all major journal-related operations.

### Constructor

```python
def __init__(self, filename="journal.txt"):
    self.filename = filename
```

The constructor stores the journal file name.

By default:

```text
journal.txt
```

is used for storing journal entries.

---

# 📁 2. File Handling

The project uses Python's built-in `open()` function to work with the journal file.

### Append Mode

```python
with open(self.filename, "a") as file:
```

The `"a"` mode is used when adding a new entry.

It adds new content to the existing file without deleting previous entries.

### Read Mode

```python
with open(self.filename, "r") as file:
```

The `"r"` mode is used to read existing journal entries.

---

# 🕒 3. Date and Time

The project imports:

```python
from datetime import datetime
```

When an entry is added, the current date and time are generated using:

```python
datetime.now()
```

The timestamp is formatted using:

```python
.strftime("%Y-%m-%d %H:%M:%S")
```

Example format:

```text
2026-09-16 10:30:25
```

Each journal entry is therefore stored with its timestamp.

---

# ➕ 4. Add New Entry

The `add_entry()` method allows the user to create a new journal entry.

```python
entry = input("Enter your journal entry: ")
```

The current timestamp is generated:

```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

The entry is then written into:

```text
journal.txt
```

The stored format is:

```text
[Timestamp] Journal Entry
```

Example:

```text
[2026-09-16 10:30:25] Completed my Python practice.
```

---

# 📖 5. View All Entries

The `view_entries()` method displays all journal entries stored in the file.

It reads the complete file:

```python
content = file.read()
```

The program checks whether the journal is empty:

```python
if content.strip() == "":
```

If there is no content:

```text
📂 Journal is empty.
```

Otherwise, all entries are displayed.

---

# 🔎 6. Search Entry

The `search_entry()` method allows the user to search the journal using:

* A keyword
* A date
* Any text contained in an entry

The user enters:

```python
keyword = input("Enter keyword or date to search: ")
```

The program reads all lines:

```python
lines = file.readlines()
```

Then each line is checked:

```python
if keyword.lower() in line.lower():
```

### Case-Insensitive Search

Using:

```python
.lower()
```

makes the search case-insensitive.

For example:

```text
Python
python
PYTHON
```

can all match the same search keyword.

---

# 🗑️ 7. Delete All Entries

The `delete_entries()` method removes the complete journal file.

Before deleting, the program asks for confirmation:

```text
Are you sure you want to delete all entries? (yes/no):
```

Only when the user enters:

```text
yes
```

does the deletion happen.

The program checks whether the file exists:

```python
os.path.exists(self.filename)
```

Then removes it using:

```python
os.remove(self.filename)
```

This provides a basic confirmation step before permanently deleting all stored journal entries.

---

# 🛡️ 8. Exception Handling

The project uses `try-except` blocks to handle errors.

For example:

```python
except FileNotFoundError:
    print("❌ Journal file does not exist yet.")
```

This prevents the program from crashing when `journal.txt` does not exist.

A general exception handler is also used:

```python
except Exception as e:
    print("❌ Error:", e)
```

---

# ⚠️ FileNotFoundError Handling

When the user tries to view or search entries before the journal file exists, the program handles the situation using:

```python
except FileNotFoundError:
```

Instead of crashing, it displays an appropriate message.

---

# 🔄 Main Menu

The `main()` function creates a `JournalManager` object:

```python
journal = JournalManager()
```

Then a `while True` loop continuously displays the menu.

```text
===== JOURNAL MANAGER =====

1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit
```

The user's choice determines which method is executed.

---

# 🔁 Program Flow

```text
              START
                │
                ▼
       Create JournalManager
                │
                ▼
          Display Menu
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
   Add Entry   View     Search
       │        │         │
       └────────┼─────────┘
                │
                ▼
          Delete Entries
                │
                ▼
              Exit?
             /     \
           No       Yes
           │         │
           └──► Menu ▼
                  END
```

---

# 📋 Features

| Feature           | Description                          |
| ----------------- | ------------------------------------ |
| ➕ Add Entry       | Saves a new journal entry            |
| 🕒 Timestamp      | Automatically records date and time  |
| 📖 View Entries   | Displays all saved entries           |
| 🔎 Search         | Searches by keyword or date          |
| 🗑️ Delete        | Deletes all journal entries          |
| ⚠️ Error Handling | Handles file and other errors        |
| 🔄 Menu System    | Provides continuous user interaction |
| 💾 File Storage   | Stores entries in `journal.txt`      |

---

# 🧪 Example Run

### Main Menu

```text
===== JOURNAL MANAGER =====
1. Add New Entry
2. View All Entries
3. Search Entry
4. Delete All Entries
5. Exit

Enter your choice (1-5):
```

### Adding an Entry

```text
Enter your journal entry: Today I learned Python file handling.

✅ Entry added successfully!
```

The file will contain an entry similar to:

```text
[2026-09-16 10:30:25] Today I learned Python file handling.
```

### Viewing Entries

```text
📖 All Journal Entries:

[2026-09-16 10:30:25] Today I learned Python file handling.
```

### Searching

```text
Enter keyword or date to search: Python

[2026-09-16 10:30:25] Today I learned Python file handling.
```

### Exiting

```text
Exiting program...
```

---

# 🧩 Important Python Functions & Methods

| Function / Method  | Purpose                         |
| ------------------ | ------------------------------- |
| `input()`          | Takes user input                |
| `print()`          | Displays output                 |
| `open()`           | Opens a file                    |
| `file.write()`     | Writes data                     |
| `file.read()`      | Reads complete file             |
| `file.readlines()` | Reads file lines                |
| `file.close()`     | Handled automatically by `with` |
| `datetime.now()`   | Gets current date and time      |
| `.strftime()`      | Formats date/time               |
| `.strip()`         | Removes surrounding whitespace  |
| `.lower()`         | Converts text to lowercase      |
| `os.path.exists()` | Checks whether file exists      |
| `os.remove()`      | Deletes a file                  |
| `try-except`       | Handles errors                  |

---

# 🏗️ OOP Structure

The project follows a simple OOP structure:

```text
JournalManager
│
├── __init__()
│
├── add_entry()
│
├── view_entries()
│
├── search_entry()
│
└── delete_entries()
```

The `main()` function handles the application's menu and user interaction.

---

# 📚 What I Learned From This Project

This project provides practical experience with:

* Python Classes
* Objects
* Constructors
* Instance Variables
* Instance Methods
* File Handling
* Reading and Writing Files
* Append Mode
* Date & Time
* String Manipulation
* Loops
* Conditional Statements
* User Input
* Exception Handling
* `os` Module
* Menu-Driven Applications

---

# 🚀 How to Run

## Step 1 — Install Python

Make sure Python 3 is installed.

Check:

```bash
python --version
```

---

## Step 2 — Save the Code

Save the Python code as:

```text
journal_manager.py
```

---

## Step 3 — Open Terminal

Navigate to the project folder:

```bash
cd path\to\Journal-Manager
```

---

## Step 4 — Run the Program

```bash
python journal_manager.py
```

The Journal Manager menu will appear.

---

# 🔮 Future Improvements

Possible future improvements for this project could include:

* Edit an existing journal entry
* Delete a single entry
* Search entries by date range
* Categorize journal entries
* Add password protection
* Store entries in CSV or JSON
* Use SQLite/MySQL database
* Add a graphical user interface
* Add analytics on journal entries
* Create a web-based journal application

---

# 💼 Data Analytics Connection

Although this is a basic Python project, it introduces concepts useful for Data Analytics.

The application demonstrates:

```text
Input Data
    ↓
Store Data
    ↓
Read Data
    ↓
Search Data
    ↓
Process Data
    ↓
Display Information
```

The same basic workflow appears in many real-world data applications, where data is collected, stored, processed, searched, and analyzed.

---

# 📌 Project Highlights

* 🐍 Python-based application
* 🏗️ Object-Oriented Programming
* 💾 Persistent text-file storage
* 🕒 Automatic timestamps
* 🔎 Keyword/date search
* 🗑️ Complete file deletion with confirmation
* 🛡️ Exception handling
* 🔄 Interactive menu-driven interface
* 📚 Practical Python programming project

---

# 👨‍💻 Author

**Hardik Kumawat**

Data Analytics Learner | Python | SQL | Excel | Power BI

---

## ⭐ Project Purpose

This project was created as a practical Python learning project to strengthen **OOP, file handling, exception handling, and menu-driven application development**.
