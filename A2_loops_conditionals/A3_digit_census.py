text = input("Enter an integer: ").strip()
digits = [character for character in text if character.isdigit()]

print("Number of digits:", len(digits))
for digit in "0123456789":
    count = digits.count(digit)
    if count:
        print(f"{digit}: {count}")
