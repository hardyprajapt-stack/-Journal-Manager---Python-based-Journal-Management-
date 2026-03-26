import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # 1️⃣ Add Entry
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"\n[{timestamp}] {entry}\n")

            print("✅ Entry added successfully!")

        except Exception as e:
            print("❌ Error while adding entry:", e)

    # 2️⃣ View All Entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("📂 Journal is empty.")
                else:
                    print("\n📖 All Journal Entries:")
                    print(content)

        except FileNotFoundError:
            print("❌ Journal file does not exist yet.")
        except Exception as e:
            print("❌ Error:", e)

    # 3️⃣ Search Entry
    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                lines = file.readlines()
                found = False

                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("❌ No matching entry found.")

        except FileNotFoundError:
            print("❌ Journal file does not exist.")
        except Exception as e:
            print("❌ Error:", e)

    # 4️⃣ Delete All Entries
    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("🗑️ All entries deleted successfully.")
                else:
                    print("❌ File does not exist.")
            except Exception as e:
                print("❌ Error:", e)
        else:
            print("Operation cancelled.")

# ---------------- MAIN MENU ----------------

def main():
    journal = JournalManager()

    while True:
        print("\n===== JOURNAL MANAGER =====")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()