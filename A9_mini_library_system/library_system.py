import csv
import json
from pathlib import Path


class Book:
    def __init__(self, title, author, copies=1):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if copies < 0:
            raise ValueError("Copies cannot be negative.")
        self.title = title.strip()
        self.author = author.strip()
        self.__copies = int(copies)

    def get_copies(self):
        return self.__copies

    def add_copies(self, count=1):
        if count <= 0:
            raise ValueError("Count must be positive.")
        self.__copies += count

    def borrow(self):
        if self.__copies == 0:
            return False
        self.__copies -= 1
        return True

    def return_copy(self):
        self.__copies += 1

    def to_dict(self):
        return {"title": self.title, "author": self.author, "copies": self.__copies}

    def __str__(self):
        return f"{self.title} by {self.author} ({self.__copies} copies)"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            existing = self.books[book.title]
            if existing.author != book.author:
                raise ValueError("A book with this title already exists with a different author.")
            if book.get_copies() > 0:
                existing.add_copies(book.get_copies())
        else:
            self.books[book.title] = book

    def show_books(self):
        if not self.books:
            print("Library is empty.")
            return
        for book in self.books.values():
            print(book)

    def borrow_book(self, title):
        book = self.books.get(title)
        if book is None:
            raise KeyError(f"Book not found: {title}")
        if not book.borrow():
            raise ValueError(f"No copies available for: {title}")
        return book

    def return_book(self, title):
        book = self.books.get(title)
        if book is None:
            raise KeyError(f"Book not found: {title}")
        book.return_copy()
        return book

    def save_json(self, filename="library.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books.values()], file, indent=4)

    def load_json(self, filename="library.json"):
        path = Path(filename)
        if not path.exists():
            raise FileNotFoundError(filename)
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        self.books = {}
        for item in data:
            self.add_book(Book(item["title"], item["author"], item["copies"]))

    def export_csv(self, filename="library.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "copies"])
            writer.writeheader()
            writer.writerows(book.to_dict() for book in self.books.values())

    @staticmethod
    def read_text_file(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


def demo():
    library = Library()
    library.add_book(Book("Python Basics", "A. Teacher", 2))
    library.add_book(Book("Learning OOP", "B. Teacher", 1))
    library.add_book(Book("Python Basics", "A. Teacher", 1))
    library.show_books()

    try:
        library.borrow_book("Python Basics")
        library.return_book("Python Basics")
    except (KeyError, ValueError) as error:
        print("Library operation failed:", error)

    library.save_json()
    library.export_csv()
    print("Saved library.json and library.csv")

    loaded = Library()
    loaded.load_json()
    print("Loaded from JSON:")
    loaded.show_books()


if __name__ == "__main__":
    try:
        demo()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print("Error:", error)
