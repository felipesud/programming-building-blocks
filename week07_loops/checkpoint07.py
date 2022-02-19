# Checkpoint Week 07: Demonstrate your understanding of loops 
#From: https://byui-cse.github.io/cse110-course/lesson07/checkpoint.html
#by: Felipe dos Santos Belisário

#01 - Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.
positive_number = 0
is_positive = False
while is_positive == False:
    positive_number = float(input('Please type a positive number: '))
    if positive_number >= 0:
        print(f'The number is: {positive_number}')
        is_positive = True
    else:
        print('Sorry, that is a negative number. Please try again. ')

#02 - Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."
child_asking = ""
may_i_have = False
while may_i_have == False:
    child_asking = input('May I have a piece of candy?').lower()
    if child_asking == 'yes':
        print('Thank You')
        may_i_have = True
    
