# Week 9 Team Activity
# Lists of Numbers
# Reference: https://byui-cse.github.io/cse110-course/lesson09/teach.html

numbers_list = []
number = ""
largest_number = 0
smallest_positive = 0

print("Enter a list of numbers, type 0 when finished.")

while number != 0:
    number = input("Enter number: ")
    
    # To prevent non numeric entries
    try:
        number = int(number)
    except:
        number = ""

    # To consider just valide entries
    if number != 0 and number != "":
        numbers_list.append(number)

        # To seek the largest number
        if number > largest_number:
            largest_number = number

        # To seek the smallest positive number
        if (number < smallest_positive or smallest_positive == 0) and number > 0:
            smallest_positive = number

# To validate if the list has any entry
if numbers_list:
    print(f"\nThe sum is: {sum(numbers_list)}")
    print(f"The average is: {sum(numbers_list) / len(numbers_list)}")
    print(f"The largest number is: {largest_number}")
    print(f"The smallest positive number is: {smallest_positive}")

    sorted_list = sorted(numbers_list)
    print("\nThe sorted list is:")

    for i in sorted_list:
        print(i)