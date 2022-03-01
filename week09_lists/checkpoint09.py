#Checkpoint Week 09 - Lists
#From: https://byui-cse.github.io/cse110-course/lesson09/checkpoint.html
#By: Felipe dos Santos Belisário

# Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

# Hint 1: You should keep asking for friends, as long as the name is not "end". (Does this sound like a loop you know?)

# Hint 2: Be careful not to add "end" to the list of names when it is typed. You can check if the name is or is not something before you add it to the list.

friend_name = ''
friends = []

while friend_name != 'end':
    friend_name = input('Type the name of a friend: ')
    friends.append(friend_name)

for friend in friends:
    if friend != 'end':
        print(friend)
