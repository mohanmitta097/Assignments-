number = int(input("Enter an integer: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not prime")
