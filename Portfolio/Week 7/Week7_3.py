"""3. Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you)."""

# Dictionary to store countries and their capital cities
country_capitals = {}

def add_country():
    """Add a new country and its capital to the dictionary."""
    country = input("Enter the name of the country: ").capitalize()
    capital = input("Enter the capital city: ").capitalize()
    country_capitals[country] = capital
    print(f"{country} and its capital {capital} added to the list.")

def display_capital():
    """Display the capital city of a given country."""
    country = input("Enter the name of the country: ").capitalize()
    if country in country_capitals:
        print(f"The capital city of {country} is {country_capitals[country]}.")
    else:
        print(f"Sorry, the capital city of {country} is not known.")

def main():
    """Main program to manage the list of countries and capitals."""
    while True:
        print("\n1. Display capital of a country")
        print("2. Add a new country and capital")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            display_capital()
        elif choice == '2':
            add_country()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()