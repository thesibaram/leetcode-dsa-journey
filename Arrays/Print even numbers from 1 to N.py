"""🌼 Problem 2: Print even numbers from 1 to N"""

while True:
    n = input("Enter a number: ")
    if not n or not n.isdigit():
        print("Invalid input")
        continue
    else:
        n = int(n)
        even_numbers = [i for i in range(n) if i % 2 == 0]
        print(even_numbers)


