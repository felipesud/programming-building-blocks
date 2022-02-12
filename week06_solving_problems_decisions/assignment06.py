#Assignment 06
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates
print('\n*                 Welcome to The Brass Plates Game!                 *\n')
user_choice = input('Like Nephi and his brothers, you need to get the brass plates from Laban. You can CONVINCE Laban to give you the plates, you can also EXCHANGE some of your family\'s treasures, or DISGUISE Laban and trick his servants into taking the plates. Make your choice. ').lower()

#Choose the user_choice
while True:
    if user_choice == 'convince':
        print('Well, let\'s negotiate with Laban\n')
        if user_choice == 'convince':
            user_choice_way1 = input('\nWell, it\'s time to face Laban. You can TALK to him or REQUIRE him to give the plates. What do you want to do?').lower()
            if user_choice_way1 == 'talk' or user_choice_way1 == 'require':
                print('Laban is a hard-hearted man, he won\'t talk to anyone who doesn\'t have riches or influence. Sorry, you won\'t be able to get the plates, please try again.')
                break
            else:
                print("\nLet's try again, type: TALK or REQUIRE\n")

            
  