# Week 05 Prove: Milestone - Adventure Game
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson05/prove.html

choice_leve1 = ""
choice_leve2 = ""
choice_leve3 = ""
choice_leve4 = ""
choice_leve5 = ""
line = "\n**********************************************\n"

print(f"{line}*       Welcome to the Adventure Game        *{line}")

## Level 1
while True:
    ### Scenario 1 - Start Here
    ### SLEEP or WATCH
    choice_leve1 = input("\nIt's 10 PM, you are watching a TV show on your cell phone, and it's starting the season's final episode. The battery is about to die, and you are feeling a little tired, so you can go to SLEEP or WATCH the final episode. What do you want to do? ").upper()
    
    if choice_leve1 == "SLEEP" or choice_leve1 == "WATCH":
        break
    else:
        print("\nLet's try again, type: SLEEP or WATCH\n")

## Level 2
while True:
    ### Scenario 2.1
    ### RISE or SNOOZE or TURN OF
    if choice_leve1 == "SLEEP":
        choice_leve2 = input('\nYou put the cell phone to charge, set up the alarm clock, and go to bed. It\'s 6:30 AM, the alarm clock is ringing, you can RISE from bed, SNOOZE the alarm clock for a few minutes, or just TURN OF the alarm. What do you want to do? ').upper()
        
        if choice_leve2 == "RISE" or choice_leve2 == "SNOOZE" or choice_leve2 == "TURN OF":
            break
        else:
            print("\nLet's try again, type: RISE or SNOOZE or TURN OF\n")
    
    ### Scenario 2.2
    ### CHARGE or RUN
    elif choice_leve1 == "WATCH":
        choice_leve2 = input("\nYou fell asleep before the episode ended. It's 9 AM, you wake up scared, your cell phone has no battery, and you think \"I'm late to work\". You can try to CHARGE a little of the battery or RUN to the work and charge it there. What do you do now? ").upper()
        
        if choice_leve2 == "CHARGE" or choice_leve2 == "RUN":
            break
        else:
            print("\nLet's try again, type: CHARGE or RUN\n")