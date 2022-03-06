#Assignment Week 09
#From: https://byui-cse.github.io/cse110-course/lesson09/prove.html
#By: Felipe dos Santos Belisário

shopping_cart = []
new_item = ''
item_add_cart = 0
id_item = 0
print('\n***********************************************')
print('*   Welcome to the Shopping Cart Program!     *')
print('***********************************************\n')

# 1. Have menu system that repeats until the user chooses quit.
while True:
    new_item = int(input('\nChoose 1,2,3'))
    if new_item == 1:
# 2. Create a list that will store the names of the items in the shopping cart.
        item_add_cart = input('\nWhat item would you like to add?').capitalize()
# 3. Complete the option to add the name of the item to the list.
        shopping_cart.append(item_add_cart)
        id_item += 1
# 4. Complete the option to display the names of the items in the list.
    elif new_item == 2:
        for i in shopping_cart:
            print(i)
    elif new_item == 3:
            print('*  Thanks for using the Shopping Cart Program!  *')
            break
    else:
        print('\nWrong choice, please, try again')




