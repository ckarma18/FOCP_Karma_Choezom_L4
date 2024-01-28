"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value"""

def read_temperatures():
    temperatures = []

    while True:
        input_temperature = input("Enter temperature in centigrade (press Enter to finish): ")

        if not input_temperature:
            break  # Exit the loop if the user presses Enter without entering a value

        if input_temperature[-1] == 'C':
            try:
                celsius_temperature = float(input_temperature[:-1])
                temperatures.append(celsius_temperature)
            except ValueError:
                print("Invalid input. Please enter a valid number followed by 'C'.")
        else:
            print("Invalid input. Please enter a number followed by 'C'.")

    return temperatures

def calculate_statistics(temperature_list):

    if temperature_list:
        max_temperature = max(temperature_list)
        min_temperature = min(temperature_list)
        mean_temperature = sum(temperature_list) / len(temperature_list)
        return max_temperature, min_temperature, mean_temperature
    else:
        return None

temperatures = read_temperatures()

statistics = calculate_statistics(temperatures)

if statistics:
    max_temperature, min_temperature, mean_temperature = statistics
    print(f"Maximum temperature: {max_temperature:.2f}C")
    print(f"Minimum temperature: {min_temperature:.2f}C")
    print(f"Mean temperature: {mean_temperature:.2f}C")
else:
    print("No valid temperatures entered.")