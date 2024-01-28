def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no(prompt):
    while True:
        response = input(prompt).upper()
        if response == 'Y' or response == 'N':
            return response
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app):
    pizza_price = 12.0
    delivery_cost = 2.5 if num_pizzas < 5 and is_delivery else 0.0
    total_price = num_pizzas * pizza_price + delivery_cost

    if is_tuesday:
        total_price *= 0.5

    if used_app:
        total_price *= 0.75

    return round(total_price, 2)

def main():
    print("BPP Pizza Price Calculator\n==========================")

    num_pizzas = get_positive_integer("How many pizzas ordered? ")

    is_delivery = get_yes_no("Is delivery required? (Y/N) ")

    is_tuesday = get_yes_no("Is it Tuesday? (Y/N) ")

    used_app = get_yes_no("Did the customer use the app? (Y/N) ")

    total_price = calculate_total_price(num_pizzas, is_delivery == 'Y', is_tuesday == 'Y', used_app == 'Y')

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
