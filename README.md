# 🚀 Personal Journal Manager

> **Project Name:** Personal Journal Manager  
> **Author:** Jenisha Ramani

A Python-based menu-driven console application designed to manage personal journal entries. The program allows users to add, view, search, and delete journal entries while automatically storing the date and time of each entry.

---

## 🎯 Project Objectives

- **🖥️ User Interface:** Create a simple menu-driven interface for managing journal entries.
- **📝 Add Entries:** Allow users to add new personal journal entries.
- **📖 View Entries:** Display all saved journal entries with their date and time.
- **🔍 Search Entries:** Search journal entries using keywords or dates.
- **🗑️ Delete Entries:** Delete all journal data while keeping the journal file.
- **📁 File Handling:** Store journal entries permanently in a text file.
- **🕒 Date & Time:** Automatically record the date and time when an entry is created.
- **⚠️ Exception Handling:** Handle file-related errors such as missing files and permission errors.

---

## ✨ Features & Functionality

1. **Add New Entry:** Allows the user to enter and save a new journal entry.
2. **View All Entries:** Displays all saved journal entries with their timestamps.
3. **Search Entry:** Finds entries based on a keyword or date.
4. **Delete All Entries:** Removes all data from the journal file without deleting the file itself.
5. **Exit:** Safely exits the Personal Journal Manager.
6. **Automatic Timestamp:** Saves the current date and time with every journal entry.
7. **Error Handling:** Handles `FileNotFoundError` and `PermissionError`.

---

## 🧠 Concepts Used

- Python Classes & Objects
- Object-Oriented Programming (OOP)
- File Handling (`open`, `read`, `write`, `append`)
- `os` Module
- `datetime` Module
- Exception Handling (`try-except`)
- User Input
- String Searching

---

## 💻 Technologies Used

- **Python 3**
- **Visual Studio Code**
- **Git & GitHub**

---

## 📂 Project Structure

```text
File_Operator/
│
├── File_Operator.py
├── journal.txt
├── output.png
└── README.md
```

### 📄 File Description

- **`File_Operator.py`** → Main Python program containing the Journal Manager.
- **`journal.txt`** → Stores the journal entries with date and time.
- **`output.png`** → Screenshot of the complete console output.
- **`README.md`** → Project documentation.

---

## 📋 Menu Options

```text
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

## 🖥️ Complete Console Output Demonstration

```text
Welcome to Personal Journal Manager!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1
Enter your journal entry: Today I learned Python.
Entry added successfully!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1
Enter your journal entry: Today I learned exception handling.
Entry added successfully!

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 2

Your Journal Entries:
------------------------------
[2026-10-01 17:49:01]
Today I learned Python.

[2026-10-01 17:49:27]
Today I learned exception handling.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 3
Enter a keyword or date to search: Python

Matching Entries:
------------------------------
[2026-10-01 17:49:01]
Today I learned Python.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 4
Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.

Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 5

Thank you for using Personal Journal Manager. Goodbye!
```

