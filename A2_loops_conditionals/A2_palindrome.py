text = input("Enter text: ")
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
