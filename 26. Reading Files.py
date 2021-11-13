
employee_file = open("employees", "r")
for employee in employee_file.readlines():
    print(employee)
"""
print(employee_file.readable()) # sprawdza czy plik może zostać odczytany
"""
# print(employee_file.readlines()[1])

employee_file.close() # zamyka plik??*

# r - read|w - write|r+ - read and write|a - appending to the file/adding to the file
