# Week 3 Team Activity
# Reference: https://byui-cse.github.io/cse110-course/lesson03/teach.html

## CORE REQUIREMENTS
pi = 3.14

square_length = float(input("What is the length of a side of the square? "))
square_area = square_length * square_length

print(f"The area of the square is {square_area}\n")

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width

print(f"The area of the rectangle is: {rectangle_area}\n")

cicle_radius = float(input("What is the radius of the circle? "))
cicle_area = pi * (cicle_radius ** 2)

print(f"The area of the circle is: {cicle_area}\n")

## STRETCH CHALLENGE 1
import math
cicle_radius = float(input("What is the radius of the circle? "))
cicle_area = math.pi * (cicle_radius ** 2)

print(f"The area of the circle is: {cicle_area}\n")

## STRETCH CHALLENGE 2
length = float(input("What is the length do you want to use? "))

print(f"The area of the square is {length * length}\n")
print(f"The area of the circle is: {math.pi * (length ** 2)}\n")
print(f"The volume of the cube is {length * length * length}\n")
print(f"The volume of the sphere is: {(4/3) * math.pi * (length ** 3)}\n")

## STRETCH CHALLENGE 3
length_cm = float(input("What is the length do you want to use in centimeter? "))
length_m = length_cm / 100

print(f"The area of the square in centimeter is {length_cm * length_cm}")
print(f"The area of the square in meters is {length_m * length_m}")
print(f"The area of the square in meters is {(length_cm * length_cm) / 10000}\n")

print(f"The area of the circle in centimeter is: {math.pi * (length_cm ** 2)}")
print(f"The area of the circle in meters is: {math.pi * (length_m ** 2)}\n")

print(f"The volume of the cube in centimeter is {length_cm * length_cm * length_cm}")
print(f"The volume of the cube in meters is {length_m * length_m * length_m}\n")

print(f"The volume of the sphere in centimeter is: {(4/3) * math.pi * (length_cm ** 3)}\n")
print(f"The volume of the sphere in meters is: {(4/3) * math.pi * (length_m ** 3)}\n")