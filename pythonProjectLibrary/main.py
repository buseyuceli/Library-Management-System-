import time
class Library:
    def __init__(self,file_name="books.txt"):
        self.file_name=file_name
        self.file=open(self.file_name,"a+")

    def __del__(self):
        self.file.close()

    def list_books(self,file_name="books.txt"):
        self.file_name=file_name
        self.file=open(self.file_name,"r")
        print("Fetching list of books...")
        time.sleep(2)
        print("****List of Books**** ")
        for line in self.file:
            book_line=line.strip().split(',')
            book_name=book_line[0]
            book_author=book_line[1]
            print(f"BOOK NAME: {book_name}, AUTHOR: {book_author}")

        self.file.close()

    def add_book(self):
        new_book_name = input("Please enter the name of the book you want to add: ")
        new_book_author = input("Please enter the author of the book you want to add: ")
        new_book_year = input("Please enter the first release year of the book you want to add: ")
        new_book_pages = input("Please enter the number of pages of the book you want to add: ")
        new_book_info = f"{new_book_name},{new_book_author},{new_book_year},{new_book_pages}\n"
        try:
            with open(self.file_name, "a") as file:
                file.write(new_book_info)
            print(f"{new_book_name} is added successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_book(self):
        removed_book_name = input("Please enter the name of the book you want to remove: ")
        found = False
        updated_lines = []
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        for line in lines:
            if not line.startswith(removed_book_name):
                updated_lines.append(line)
            else:
                found = True

        with open(self.file_name, "w") as file:
            for line in updated_lines:
                file.write(line)

        if found:
            print(f"{removed_book_name} found and removed successfully.")
        else:
            print(f"{removed_book_name}, cannot found")

lib=Library()

while True:
    print("***MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    menu_item=input("Please select a menu item (1-3, q to quit): ")

    if menu_item=="1":
        lib.list_books()
    elif menu_item=="2":
        lib.add_book()
    elif menu_item=="3":
        lib.remove_book()
    elif menu_item=="q":
        print("Exiting...")
        break
    else:
        print("Invalid menu item. Please select a number between 1 and 3: ")







