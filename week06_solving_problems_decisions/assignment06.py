#Assignment 06
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates
user_choice_way = ""
user_choice = ""

print('\n*                 Welcome to The Brass Plates Game!                 *\n')
while True:
    user_choice = input('\nLike Nephi and his brothers, you need to get the brass plates from Laban. You can CONVINCE Laban to give you the plates, you can also EXCHANGE some of your family\'s treasures, or DISGUISE Laban and trick his servants into taking the plates. Make your choice. ').lower()
    if user_choice == 'convince' or user_choice == 'exchange' or user_choice == 'disguise':
        break
    else:
        print("\nLet's try again, please, type: CONVINCE, EXCHANGE or DISGUISE\n")
#Choose the user_choice
while True:
    #1st way
    if user_choice == 'convince':
        print('\nWell, let\'s negotiate with Laban\n')
        user_choice_way = input('\nWell, it\'s time to face Laban. You can TALK to him or REQUIRE him to give the plates. What do you want to do?').lower()
        if user_choice_way == 'talk' or user_choice_way == 'require':
            print('\nLaban is a hard-hearted man, he won\'t talk to anyone who doesn\'t have riches or influence. Sorry, you won\'t be able to get the plates, please try again.')
            break
        else:
            print("\nLet's try again, please, type: TALK or REQUIRE\n")
    
    #2nd way
    if user_choice == 'exchange':
       print('\nYes!, let\'s show your money to Laban!')
       user_choice_way = input('\nYou went to your house and got all kinds of gold and precious things to exchange for the plates. Now you have 2 options, you can take EVERYTHING to Laban or you can SAVE some for a future counter-proposal. What do you prefer?').lower()
       if user_choice_way == 'everything':
           print('\nLaban is very ambitious, he became interested in your treasure and ordered his guards to steal it. Too bad, you lost your money and ran out of plates. Game Over')
           break
    if user_choice_way == 'save':
        user_choice_way2 = input('\nYou are a negotiator! Laban got interested and made a low offer, you now have a chance to RAISE the offer or FOLD. What do you want to do?').lower()
        if user_choice_way2 == 'raise':
            print('Great! Laban accepted the offer and handed over the plates, now you can return to your father\'s tent ')
        else:
            print('\nIn such a negotiation you cannot be afraid. Laban sensed your fear and ordered his guards to steal all of your treasure. Too bad, you lost your money and ran out of plates. Game Over')        
            break

