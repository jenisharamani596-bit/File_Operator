import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # 1. Add New Entry
    def add_entry(self):
        entry = input("\nEnter your journal entry: ")

        try:
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{date_time}]\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("\nError: Permission denied.")

    # 2. View All Entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()

            if content:
                print("\nYour Journal Entries:")
                print("------------------------------")
                print(content)
            else:
                print("\nNo journal entries found.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied.")

    # 3. Search Entry
    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                content = file.read()

            entries = content.split("\n\n")
            found = False

            print("\nMatching Entries:")
            print("------------------------------")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied.")

    # 4. Delete All Entries
    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                with open(self.filename, "w") as file:
                    file.write("")

                print("\nAll journal entries have been deleted.")

            except PermissionError:
                print("\nError: Permission denied.")

        else:
            print("\nDelete operation cancelled.")


# Main Program
journal = JournalManager()

print("Welcome to Personal Journal Manager!")

while True:

    print("\nPlease select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nUser Input: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("\nInvalid option. Please select a valid option from the menu.")