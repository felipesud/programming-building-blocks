age = input('Please type your age: ')
birthday = int(age) + 1

print(f"How old are your? {str(age)}")
print(f"On your next birthday, you will be {str(birthday)}")


cartons = input('Please type the number of egg cartons you have: ')
eggs = int(cartons)*12

print(f"\nHow many egg cartons do you have? {str(cartons)}")
print(f"You have {str(eggs)} eggs")

cookies = input('Please enter the number of cookies: ')
people = input('Type the number of people: ')
division = float(cookies) / float(people)

print(f"\nHow many cookies do you have? {str(cookies)}")
print(f"How many people are there? {str(people)}")
print(f"Each person may have {str(division)} cookies")