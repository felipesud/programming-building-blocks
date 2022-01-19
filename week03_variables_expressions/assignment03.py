c_meal = input('What is the price of a child\'s meal?')
a_meal = input('What is the price of an adult\'s meal?')
children = input('How many children are there?')
adults = input('How many adults are there?')
tax_rate = input('What is the sales tax rate?')
print(f"What is the price of a child\'s meal? ${c_meal}")
print(f"What is the price of an adult\'s meal? ${a_meal}")
print(f"How many children are there? {children}")
print(f"How many adults are there? {adults}")
print(f"What is the sales tax rate? {tax_rate}")
subtotal = 0
sales_tax = 0
total = 0
print(f"\nSubtotal: {subtotal}")
print(f"Sales Tax: {sales_tax}")
print(f"Total: {total}")

payment = input('\nWhat is the payment amount?')
change = float(payment) - float(total)
print(f"Change: ${change}")