#Assignment 06
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates
print('Welcome to The Brass Plates Game!\n')
way = input('Please, type NEGOTIATION if you want to negotiate with Laban, type TREASURE if you want to exchange your treasure with plates or type DISGUISE if you want to use the Laban clothes to take the plates: ').lower()
user_name = input('Type here your name: ').capitalize()
#Choose the way
if way == 'negotiation':
    print('Well, let\'s negotiate with Laban\n')
elif way == 'treasure':
    print('Yes!, let\'s show your money to Laban!\n')
elif way == 'disguise':
    print('Here are Laban\'s clothes, hurry up, get dressed\n')
else:
    print('Wrong answer, Please type again\n')

#The Game
#1st way chosen
if way == 'negotiation':
    print('Laban: "Who are you? What do you want?')
    print(f'Hi, my name is {user_name} and.... I want to get the Brass Plates, could you give them to me? ')
    print('Laban: How dare you come to me and ask for the plates? Guards! get him!!!!')
    run_out = input('Please type RUN to go out the Laban\'s house').lower()
    if run_out == 'run':
        print('Bad news, you didn\'t get the plates, try again.')
    else:
        print('You didn\'t run! The guards got you. \n Game Over')
elif way == 'treasure':
    print('Laban: "Who are you? What do you want?')

