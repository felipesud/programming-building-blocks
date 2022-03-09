#Assignment Week 10
#From: https://byui-cse.github.io/cse110-course/lesson09/prove.html
#By: Felipe dos Santos Belisário
import math

items_cart = []
prices_cart = []
new_item = ''
price_new_item = 0
item_add_cart = 0

print('\n***********************************************')
print('*   Welcome to the Shopping Cart Program!     *')
print('***********************************************\n')


while True:
    print(
        "\nPlease select one of the following: \n" \
        "1. Add item\n" \
        "2. View cart\n" \
        "3. Remove item\n" \
        "4. Compute total\n" \
        "5. Quit\n" \
    )
    new_item = int(input('Please enter an action: '))
    if new_item == 1:
        item_add_cart = input('\nWhat item would you like to add?').capitalize()
        price_new_item = float(input(f'What is the price of "{item_add_cart}"?'))
        items_cart.append(item_add_cart)
        prices_cart.append(price_new_item)
        print(f'"{item_add_cart}" has been added to the cart')
     
    elif new_item == 2:
        print('The contents of the shopping cart are: ')    
        for i in range(len(items_cart)):
            item = items_cart[i]
            price = prices_cart[i]
            print(f'{i + 1}.{item} - ${price:.2f}')
    elif new_item == 3:
        to_remove = int(input('Which item would you like to remove? ')) - 1
        items_cart.pop(to_remove)
        prices_cart.pop(to_remove)
        print('Item removed successfully.')
    elif new_item == 4:
        sum_prices = sum(prices_cart)
        print(f'The total price of the items in the shopping cart is: {sum_prices:.2f}')
    elif new_item == 5:
        print('Thank you for using the Shopping Cart Program! Goodbye')
        break
    else:
        print('\nWrong choice, please, try again')

