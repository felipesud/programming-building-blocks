#Assignment Week 10
#From: https://byui-cse.github.io/cse110-course/lesson09/prove.html
#By: Felipe dos Santos Belisário

items_cart = []
prices_cart = []
items_quantities = []
new_item = ''
price_new_item = 0
item_add_cart = 0
item_amount = 0
to_remove = 0

print('\n=================================================')
print('*                THE SHOPPING CART                 *')
print('=================================================\n')

#A menu system that repeats until the user chooses quit.
while True:
    print(
        "\nPlease select one of the following: \n" \
        "1. Add item\n" \
        "2. View cart\n" \
        "3. Remove item\n" \
        "4. Compute total\n" \
        "5. Quit\n" \
    )
   #The user will insert the NAME, AMOUNT (Exceeding requirements) and PRICE of the item
    new_item = int(input('Please enter an action: '))
    if new_item == 1:
        item_add_cart = input('What item would you like to add?').capitalize()
        item_amount = int(input(f'How many {item_add_cart} do you want? '))
        price_new_item = float(input(f'What is the price of "{item_add_cart}"?'))
        items_quantities.append(item_amount)
        items_cart.append(item_add_cart)
        prices_cart.append(price_new_item)
        print(f'"{item_add_cart}" has been added to the cart')
    #The system will show up the INDEXES (+1 to avoid the zero), NAME, AMOUNT, PRICE and the TOTAL (Exceeding requirements) 
    elif new_item == 2:
        print('The contents of the shopping cart are: ')    
        for i in range(len(items_cart)):
            item = items_cart[i]
            price = prices_cart[i]
            amount = items_quantities[i]
            print(f'{i + 1}.{item} - {amount} units for ${price:.2f} - Total: ${amount * price:.2f}')
     #The system will request wich item to remove, the user type the number. To find the right index, i did user_choice -1 (line 48)      
    elif new_item == 3:
         to_remove = int(input('Which item would you like to remove? ')) - 1
         while len(items_cart) >= to_remove:
                
                #With variable which_item I can show the name of item that were deleted, see on line 54
                which_item = items_cart[to_remove]
                items_cart.pop(to_remove)
                prices_cart.pop(to_remove)
                items_quantities.pop(to_remove)
                #print the result of operation to the user
                print(f'{which_item} removed successfully.')
                break  
         else:
                print('Please, enter a correct number')
    elif new_item == 4:
        #In this case I just did total of prices using the sum function.
        sum_prices = sum(prices_cart)
        print(f'The total price of the items in the shopping cart is: {sum_prices:.2f}')
    elif new_item == 5:
        print('\nThank you Goodbye')
        break
    else:
        print('\nWrong choice, please, try again')

