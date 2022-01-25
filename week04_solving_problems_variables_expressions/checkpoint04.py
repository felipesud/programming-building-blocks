#CHECKPOINT 04
#The Problem: Converting between different types of units
#From: https://byui-cse.github.io/cse110-course/lesson04/checkpoint.html

temperature = float(input('What is the temperature in Fahrenheit? '))
conversion = (temperature - 32) * (5 / 9)

print(f'The temperature in Celsius is {conversion:.1f} degrees')