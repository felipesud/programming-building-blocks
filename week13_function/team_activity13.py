#Team Activity Week 13 - Function Basics
#From: https://byui-cse.github.io/cse110-course/lesson13/teach.html
#By: Group 4 

import math

def compute_area_square(square_length):
    return square_length * square_length

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(circle_radius):
    return math.pi * (circle_radius ** 2)

def compute_area(shape, value, second_value=0):
    area = None
    
    if shape == "square":
        area = compute_area_square(value)
    elif shape == "rectangle":
        area = compute_area_rectangle(value, second_value)
    elif shape == "circle":
        area = compute_area_circle(value)
    
    return area

option = None
while option != "quit":

    print("\nwhat kind of shape do you have? \n- square\n- rectangle\n- circle\n")
    option = input("Please enter a shape or quit to exit: ").lower().strip()

    if option == "square":
        length = float(input("\nWhat is the length of a side of the square? "))
        
        print(f"The area of the square is {compute_area(option, length)}\n")
    elif option == "rectangle":
        length = float(input("\nWhat is the length of rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        
        print(f"The area of the rectangle is: {compute_area(option, length, width)}\n")
    elif option == "circle":
        radius = float(input("\nWhat is the radius of the circle? "))
        
        print(f"The area of the circle is: {compute_area(option, radius):.2f}\n")
    elif option == "quit":
        print("Thank you!")