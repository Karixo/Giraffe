
try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  # good practice
    print(err)
except ValueError:
    print("Invalid input")
