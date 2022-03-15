#Checkpoint Week 10 Solving Problems Using Lists
#From: https://byui-cse.github.io/cse110-course/lesson10/checkpoint.html
#By: Felipe dos Santos Belisário

#Assignment:
# Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly.

# Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk

# Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.

shopping_list = []
user_item = ""

while user_item != 'quit':
    user_item = input('Please enter the items of the shopping list (type: quit to finish):').lower()
    if user_item != 'quit':
        shopping_list.append(user_item)

print(f'\n The shopping list is:')
for item in shopping_list:
    print(item.capitalize())

print(f'\n The shopping list with indexes is: ')
for i in range(len(shopping_list)):
    item = shopping_list[i].capitalize()    
    print(f'{i}. {item}')



index_chosen = int(input('Wich item would you like to change? '))
new_item = input('Wich is the new item? ')

shopping_list[index_chosen] = new_item

print(f'\n The shopping list UPDATED with indexes is: ')   
for i in range(len(shopping_list)):
    item = shopping_list[i].capitalize()
    print(f'{i}. {item}')