c_meal = input('What is the price of a child\'s meal?')
a_meal = input('What is the price of an adult\'s meal?')
children = input('How many children are there?')
adults = input('How many adults are there?')
tax_rate = input('What is the sales tax rate?')
subtotal = 0
sales_tax = 0
total = 0
print(f"\nSubtotal: {subtotal}")
print(f"Sales Tax: {sales_tax}")
print(f"Total: {total}")

payment = input('\nWhat is the payment amount?')
change = float(payment) - float(total)