"""Write a program that takes a centigrade temperature and displays the equivalent in
Fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

input_temperature = input("Enter the temperature in centigrade: ")

if input_temperature[-1] == 'C':
    try:
        celsius_temperature = float(input_temperature[:-1])
        fahrenheit_result = celsius_to_fahrenheit(celsius_temperature)
        print(f"The equivalent temperature in Fahrenheit: {fahrenheit_result:.2f}F")
    except ValueError:
        print("Invalid input. Please enter a valid number followed by 'C'.")
else:
    print("Invalid input. Please enter a number followed by 'C'.")