''' Write a program that reads 6 temperatures (in the same format as before), and
   displays the maximum, minimum, and mean of the values.
   Hint: You should know there are built-in functions for max and min. If you hunt, you
   might also find one for the mean.'''

def read_temperatures():
    temperatures = []

    for i in range(6):
        input_temperature = input(f"Enter temperature {i + 1} in centigrade (e.g., 25C): ")

        if input_temperature[-1] == 'C':
            try:
                celsius_temperature = float(input_temperature[:-1])
                temperatures.append(celsius_temperature)
            except ValueError:
                print(f"Invalid input for temperature {i + 1}. Please enter a valid number followed by 'C'.")
        else:
            print(f"Invalid input for temperature {i + 1}. Please enter a number followed by 'C'.")

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