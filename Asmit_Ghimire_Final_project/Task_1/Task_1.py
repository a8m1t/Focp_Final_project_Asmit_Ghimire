
def calculate_total_cost(no_of_pizzas,is_delivery,is_tuesday,used_app):
    pizza_price = 12.0
    delivery_cost = 2.50
    app_discount = 0.25
    tuesday_discount = 0.5
    
    total_price= no_of_pizzas*pizza_price

    if is_tuesday:
        total_price-=total_price*tuesday_discount

    if is_delivery and no_of_pizzas<5:
        total_price=total_price+delivery_cost
    
    if used_app:
        total_price-=total_price*app_discount
    return total_price

def get_valid_input(prompt, valid_responses):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_responses:
            return user_input
        else:
            print('Please answer in "y","n"')

def main():
    print("BPP pizza price calculator")
    print("===========================")

    while True:
        try:
            no_of_pizzas = int(input("How many pizzas ordered? "))
            if no_of_pizzas >= 0:
                break
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

    is_delivery = get_valid_input("Is delivery required? (y/n) ", ['y', 'n']) == 'y'

    is_tuesday = get_valid_input("Is it Tuesday? (y/n) ", ['y', 'n']) == 'y'

    used_app = get_valid_input("Did the customer use the app? (y/n) ", ['y', 'n']) == 'y'

    total_cost=calculate_total_cost(no_of_pizzas,is_delivery,is_tuesday,used_app)
    print(f"The total price is:£{total_cost:.2f}")


if __name__ == "__main__":
    main()

