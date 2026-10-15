import csv
import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = None
        self.set_marks(marks)

    def set_marks(self, marks):
        if not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
            raise ValueError("Marks must be a number from 0 to 100.")
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        return "F"

    def __str__(self):
        return f"{self.name}: {self.__marks}/100 — Grade {self.grade()}"

    def to_dict(self):
        return {"name": self.name, "marks": self.__marks, "grade": self.grade()}


def write_student_files(students):
    with open("students.txt", "w", encoding="utf-8") as file:
        for student in students:
            file.write(str(student) + "\n")

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "marks", "grade"])
        writer.writeheader()
        writer.writerows(student.to_dict() for student in students)

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)


def read_marks_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                value = line.strip()
                if not value:
                    continue
                try:
                    marks = float(value)
                except ValueError:
                    raise ValueError(f"Invalid marks on line {line_number}: {value}")
                if not 0 <= marks <= 100:
                    raise ValueError(f"Marks out of range on line {line_number}: {value}")
                print(marks)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except ValueError as error:
        print(f"Invalid marks data: {error}")
    finally:
        print("File operation finished.")


if __name__ == "__main__":
    students = [
        Student("YOUR NAME", 88),  # Replace YOUR NAME with your own name.
        Student("Student Two", 74),
        Student("Student Three", 39),
    ]

    try:
        students[0].set_marks(150)
    except ValueError as error:
        print("Validation works:", error)

    for student in students:
        print(student)

    write_student_files(students)
    print("\nRead text file:")
    with open("students.txt", "r", encoding="utf-8") as file:
        print(file.read())

    print("Read CSV file:")
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        print(list(csv.DictReader(file)))

    print("Read JSON file:")
    with open("students.json", "r", encoding="utf-8") as file:
        print(json.load(file))

    # Demonstrate valid file, missing file, and invalid marks file.
    with open("marks_valid.txt", "w", encoding="utf-8") as file:
        file.write("85\n70\n")
    with open("marks_invalid.txt", "w", encoding="utf-8") as file:
        file.write("85\nnot-a-number\n")

    read_marks_file("marks_valid.txt")
    read_marks_file("missing_marks.txt")
    read_marks_file("marks_invalid.txt")
