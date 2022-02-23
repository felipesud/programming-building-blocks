#Checkpoint week 08 - Solving Problems Using Loops
#From: https://byui-cse.github.io/cse110-course/lesson08/checkpoint.html
#By: Felipe dos Santos Belisário

#01 - Use a for loop to iterate through this list one by one and display each item on its own line
print('Use a for loop to iterate through this list one by one and display each item on its own line')
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)
   


#Use a for loop to display the numbers 1–8, one number on each line
print('\nUse a for loop to display the numbers 1–8, one number on each line')
for numbers in range(9):
    print(numbers)



#Use a for loop to display the even numbers (hint: count by two) 2–20, one number on each line 
print('\nUse a for loop to display the even numbers (hint: count by two) 2–20, one number on each line ')
for even_numbers in range(2, 22, 2):
    print(even_numbers)