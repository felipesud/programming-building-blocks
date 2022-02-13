can_ride = False
rider2_age = 0
rider2_height = 0
rider1_age = int(input("What is the age of the first rider?"))
rider1_height = float(input("What is the height of the first rider?"))
has_rider2 = input("Is there a second rider (yes/no)?").lower()
if has_rider2 == "yes":
    rider2_age = int(input("What is the age of the second rider?"))
    rider2_height = float(input("What is the height of the second rider?"))
else: 
    if rider1_age > 17 and rider1_height > 61:
        can_ride = True
if rider1_height > 35 and rider2_height > 35:
    if rider1_age > 17 or rider2_age > 17: 
        can_ride = True

if can_ride:
    print("Welcome to the ride. Please be safe and have fun")
else: 
    print("Sorry, you may not ride.")

    