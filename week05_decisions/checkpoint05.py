#Write a program that asks the user for two integers.
#From:  https://byui-cse.github.io/cse110-course/lesson05/checkpoint.html
#By: Felipe dos Santos Belisário

#Declaring Variables
first_num = int(input('Please type a number '))
second_num = int(input('Please type another number '))

# Check: If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater"
if first_num > second_num:
    print('\nThe first number is greater')
else: 
    print('The first number is not greater')

# Check: If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".
if first_num == second_num:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

# Check: If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".
if second_num > first_num:
    print('The second number is greater')
else:
    print('The second number is not greater\n')



# COMPARING STRINGS
#Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

animal = input('What is your favorite animal? ')

if animal.lower() == 'gato':
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')
