# Assignment-wise explanations (beginner friendly)

## A1 — First programs
- `print_name.py`: gets a name with `input()` and displays it.
- `greatest_of_four.py`: stores four entered numbers in a list and uses `max()`.
- `ticket_price.py`: demonstrates `if / elif / else`. The PDF does not specify the exact age/price slabs, so the values are examples and should be replaced with the class rules.
- `electricity_bill.py`: demonstrates slab-based calculation. The PDF does not specify the rates, so replace the example rates with the class rules.

## A2 — Loops and conditional branching
- Reverse: builds a reversed string one character at a time.
- Palindrome: normalizes the text and compares it with its reverse.
- Digit census: counts digit characters and reports each digit that occurs.
- Prime: checks divisors up to the square root.
- Multiplication grid: nested loops print products in a grid.
- Number pyramid: outer loop controls rows; inner loop prints numbers.
- Part B selection: this package chooses GCD. The Euclidean algorithm repeatedly replaces `(a, b)` with `(b, a % b)` until `b` is zero.
- `C1_explanation.txt` contains the written reflection.

## A3 — Lists and strings
- `cities.py`: repeatedly collects city names, prints them, and optionally removes one.
- `favourite_items.py`: collects five favourite items into a list.
- `subject_marks.py`: collects ten marks and calculates maximum, minimum, and average.
- `count_vowels.py`: counts a/e/i/o/u without case sensitivity.
- `palindrome_slicing.py`: uses `[::-1]` to reverse a string.

## A4 — List comprehensions
`pass_fail.py` creates a new list in one expression. The example uses 40 as the pass mark; change it if your trainer gave a different threshold.

## A5a — Bank class
`Bank` stores the balance in `__balance`, which is a private-style attribute. `deposit()` adds money, `withdraw()` refuses an amount above the balance, and `get_balance()` returns the current balance.

## A5b — Library homework
`Book` stores its copy count privately and defines `__str__`. `Library` combines duplicate titles by increasing copies, lists books, refuses borrowing when no copies remain, and supports returns.

## A6 — File handling
The program writes and reads:
- a plain text file, one name per line;
- a CSV file with `csv.DictWriter` and reads it with `csv.DictReader`;
- a JSON file with `json.dump` and reads it with `json.load`.

## A7 — OOP, files, and exceptions
- `Student` validates marks from 0 through 100.
- `grade()` assigns a grade using example boundaries; change them if your trainer specified different boundaries.
- `__str__()` makes a student object readable when printed.
- The program writes and reads text, CSV, and JSON files.
- `read_marks_file()` handles `FileNotFoundError` and `ValueError` separately and always prints the required finally message.
- Replace `YOUR NAME` before running.

## A8 — Missing Fest Trophy
`Player` stores collected items in a bag. `Place` can be locked and require an item. `Chest` checks a code. The script runs the failed route first, then the winning route, demonstrating that object state affects the story.

## A9 — Mini Library System
`Book` manages a title, author, and private copy count. `Library` adds books without duplicating a title, borrows and returns books, saves/loads JSON, exports CSV, and includes a text-file reader. The `check.py` script runs basic assertions. Run it from the A9 folder with `python check.py`.

## Before pushing to GitHub
Run each script, fix any issue you encounter, replace placeholder names, and complete `AI_USAGE.md` truthfully. The PDF says A9 must be pushed when the checker is green and that the repository link should be shared with the group.
