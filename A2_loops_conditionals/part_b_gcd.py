# Selected Part B task: greatest common divisor (GCD)
first = abs(int(input("Enter the first integer: ")))
second = abs(int(input("Enter the second integer: ")))

while second != 0:
    first, second = second, first % second

print("GCD:", first)
