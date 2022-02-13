#Assignment 06
#From: https://byui-cse.github.io/cse110-course/lesson05/prove.html
#By: Felipe dos Santos Belisário

#Looking for Brass Plates
user_choice = ""
user_choice_way = ""
user_choice_way2 = ""
user_choice_way3 = ""
user_choice_way4 = ""
user_choice_way5 = ""
user_choice_way6 = ""

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
            elif user_choice_way2 == 'fold':
                print('\nIn such a negotiation you cannot be afraid. Laban sensed your fear and ordered his guards to steal all of your treasure. Too bad, you lost your money and ran out of plates. Game Over')        
            break
        else:
            print("\nLet's try again, please, type: EVERYTHING or SAVE\n")
    
    #3rd way
    if user_choice == 'disguise':
        user_choice_way2 = input('\nCool, you took advantage of Laban\'s absence and got dressed. The problem is that he will arrive soon, you have to be fast. You can RUN and do everything in a hurry, you can also impersonate Laban and SEND the servants to get the plates for you, or you can ENJOY and get Laban\'s sword for you before taking the plates.').lower()
        if user_choice_way2 == 'run':
            print('Well done! You got the plates in time before Laban returned. Congratulations, now you can go back to your father\'s tent. ')
            break    
        elif user_choice_way2 == 'send':
            user_choice_way3 = input('\nFor the servant not to distrust you, take the SWORD or IMITATE the voice of Laban. Please choose a way forward').lower()
            if user_choice_way3 == 'sword':
                print('Zoran the servant is scared. You reassured him, you took the signs, and now you and he will return to your father\'s tent.')
                break
            elif user_choice_way3 == 'imitate':
                user_choice_way4 = input('\nWhen ordering the servants to take the plates, you can either be SEVERE in your words or POLITE. How do you want to speak?').lower()
                if user_choice_way4 == 'severe':
                    print('\nVery well, this is how Laban treats his servants, no one suspected you, the servants took the plates, gave them to you. Now you can go back to your father\'s tent.')
                    break
                elif user_choice_way4 == 'polite':
                    user_choice_way5 = input('\nThe servants noticed something strange, as Laban is not usually so polite. They saw you\'re an imposter and they want to arrest you. You can ESCAPE them or HIDE yourself to try and get the plates somehow.').lower()
                    if user_choice_way5 == 'escape':
                        print('\nUnfortunately, your cover didn\'t work and you didn\'t manage to get the plates. Try again.')
                        break
                    elif user_choice_way5 == 'hide':
                        user_choice_way6 = input('\nNow you are hidden. Laban seems to be getting home, you need to be quick. Wait for Laban to arrive, you take the plates and sneak out the WINDOW, or you can grab the SWORD and fight the guards. What do you choose?').lower()
                        if user_choice_way6 == 'window':
                            print('\nCongratulations on your courage, you were smart and took the plates even though you were in an adverse situation.')
                            break
                        elif user_choice_way6 == 'sword':
                            print('\nAlone against all those guards, it would be impossible to win, wouldn\'t it? You were caught by the guards. Game Over')
                            break

