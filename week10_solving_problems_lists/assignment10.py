#Assignment Week 10
#From: https://byui-cse.github.io/cse110-course/lesson09/prove.html
#By: Felipe dos Santos Belisário

items_cart = []
prices_cart = []
new_item = ''
price_new_item = 0
item_add_cart = 0

print('\n***********************************************')
print('*   Welcome to the Shopping Cart Program!     *')
print('***********************************************\n')

# 1. Have menu system that repeats until the user chooses quit
while True:
    new_item = int(input(
        "Please select one of the following: \n" \
        "1. Add item\n" \
        "2. View cart\n" \
        "3. Remove item\n" \
        "4. Compute total\n" \
        "5. Quit\n" \
    ))
    if new_item == 1:
        item_add_cart = input('\nWhat item would you like to add?').capitalize()
        price_new_item = float(input(f'What is the price of "{item_add_cart}"?'))
        items_cart.append(item_add_cart)
        prices_cart.append(price_new_item)
     
    elif new_item == 2:
        for i in items_cart:
            print(i)
    elif new_item == 3:
            print('*  Thanks for using the Shopping Cart Program!  *')
            break
    else:
        print('\nWrong choice, please, try again')




