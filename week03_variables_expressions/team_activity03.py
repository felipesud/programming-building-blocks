import math
# AREA OF THE SQUARE => Area = Length * Length or Area = Length ** 2
squ_length = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {squ_length ** 2}')

# AREA OF THE RECTANGLE => Area = Length * Width
rec_length = float(input('What is the length of rectangle? '))
rec_width = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {rec_length * rec_width}')

# AREA OF THE CIRCLE => Area = Pi * (Radius ** 2)
rad_circle = float(input('What is the radius of the circle?'))
print(f'The area of the circle is: {math.pi * (rad_circle ** 2):.4f}')

# STRETCH CHALLENGE
print('\n------------------------------------------------------------------------------')
print('\nSTRETCH CHALLENGE\n')
single_length = float(input('Please type a single length: '))

# Square Area A = l ** 2
square_area = single_length ** 2
print(f'The square is: {square_area:.2f}')

# Circle Area A = Pi * (r ** 2)
circle_area = math.pi * (single_length ** 2)
print(f'The circle area is: {circle_area:.2f}')

# Cube Volume V = l ** 3
cube_volume = single_length ** 3
print(f'The volume of the cube is: {cube_volume:.2f}')

# Sphere Volume  V = 4/3 Pi * r ** 3
sph_volume = (4 / 3) * math.pi * (single_length ** 3)
print(f'The volume of the sphere is: {sph_volume:.2f}')
print('\n------------------------------------------------------------------------------')
