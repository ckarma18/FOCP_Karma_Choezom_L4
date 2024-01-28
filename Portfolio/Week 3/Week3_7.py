"""Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive"""

table_number = int(input("Enter the number for the times table from 0-12: "))

if 0 <= table_number <= 12:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    print("Invalid input. Please enter a number between 0 and 12 inclusive.")