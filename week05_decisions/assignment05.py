#Assignment 05
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates

way = input('Please, type NEGOTIATION if you want to negotiate with Laban, type TREASURE if you want to exchange your treasure with plates or type DISGUISE if you want to use the Laban clothes to take the plates: ')

if way.lower() == 'negotiation':
    print('Well, let\'s negotiate with Laban')
elif way.lower() == 'treasure':
    print('Yes!, let\'s show your money to Laban!')
elif way.lower() == 'disguise':
    print('Here are Laban\'s clothes, hurry up, get dressed')
else:
    print('Wrong answer, Please type again')