"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in Fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is equivalent to {fahrenheit_result:.2f} Fahrenheit")

fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equivalent to {celsius_result:.2f} Celsius")