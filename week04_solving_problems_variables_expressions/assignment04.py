# ASSIGNMENT 04
# Meal Price Calculator
# From: https://byui-cse.github.io/cse110-course/lesson03/prove.html
#      https://byui-cse.github.io/cse110-course/lesson04/prove.html
# By: FELIPE DOS SANTOS BELISÁRIO

#Variables and inputs
meal_c = float(input('What is the price of a child\'s meal?'))
meal_a = float(input('What is the price of an adult\'s meal?'))
dessert_price = float(input('What is the price of a dessert'))
desserts = int(input('How many desserts were served?'))
children = int(input('How many children are there?'))
adults = int(input('How many adults are there?'))
tax_rate = float(input('What is the sales tax rate?'))

print('\n Restaurant ZION\'S PATHWAY')
print('\n ORDER ')
print(' =========================================================== \n')

# Outputs - Messages for the user
print(f"\nWhat is the price of a child\'s meal? ${meal_c}")
print(f"What is the price of an adult\'s meal? ${meal_a}")
print(f"What is the price of a dessert ${dessert_price}")
print(f"How many desserts were served? {desserts}")
print(f"How many children are there? {children}")
print(f"How many adults are there? {adults}")
print(f"What is the sales tax rate? {tax_rate}")
print('\n =========================================================== \n')

# Calculating the subtotal and total
subtotal = (meal_c * children) + (meal_a * adults) + (dessert_price * desserts)
tip = subtotal * 0.10
sales_tax = subtotal * (tax_rate / 100)
total = subtotal + sales_tax + tip

# Showing to the user how much he/she needs to pay
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"10% Tip for the Waiter: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

# Calculating the change
payment = float(input('What is the payment amount?'))
change = payment - total
print(f"Change: ${change:.2f}")
print('\n =========================================================== \n')
