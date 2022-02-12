#Assignment 05
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates
print('Welcome to The Brass Plates Game!\n')
way = input('Please, type NEGOTIATION if you want to negotiate with Laban, type TREASURE if you want to exchange your treasure with plates or type DISGUISE if you want to use the Laban clothes to take the plates: ')
user_name = ""
#Choose the way
if way.lower() == 'negotiation':
    print('Well, let\'s negotiate with Laban\n')
elif way.lower() == 'treasure':
    print('Yes!, let\'s show your money to Laban!\n')
elif way.lower() == 'disguise':
    print('Here are Laban\'s clothes, hurry up, get dressed\n')
else:
    print('Wrong answer, Please type again\n')

#The Game
#1st way chosen
if way.lower() == 'negotiation':
    print('Laban: "Who are you? What do you want?')
    user_name = input('Type here your name')
    print(f'Hi, my name is {user_name.capitalize()} and.... I want to get the Brass Plates, could you give them to me? ')

    