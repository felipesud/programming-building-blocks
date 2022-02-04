#Team Activity Week 05
#From: https://byui-cse.github.io/cse110-course/lesson05/teach.html

#Write a program that determines the letter grade


grade = float(input('Please, type your grade here '))
remainder = grade % 10
sign = ""

#Check the signal after the grade
if remainder >= 7:
    sign = '+'
elif remainder < 3:
    sign = '-'

#Chack the grade
letter = ""
# A >= 90
if grade >= 90:
    letter = 'A'
    if remainder > 3:
        sign = ""
# B >= 80
elif grade >= 80:
    letter = 'B'
# C >= 70
elif grade >= 70:
    letter = 'C'
# D >= 60
elif grade >= 60:
    letter = 'D'
# F < 60
else:
    letter = 'F'
    sign = ""
#Show grade
print(f'Your grade is: {letter}{sign}')

# Show the result
if grade >= 70:
    print('Congratulations!! You passed')
else:
    print('Oh no you failed')
    

