number = int(input("How many columns and rows do you want in your multiplication table? ")) + 1

space = len(str(number * number))
    
for line in range (1, number):
    for column in range (1, number):
        print(f"{(line * column):{space}}", end=" ")
    print()