#Assignment Week 08 - Solving Problems Using Loops
#From: https://byui-cse.github.io/cse110-course/lesson07/prove.html
#By: Felipe dos Santos Belisário


from PIL import Image
#Call Images
picture_one = Image.open('./cat_small.jpg')
picture_two = Image.open('./forest.jpg')


#Pick-up the Image sizes
cat_small_width, cat_small_height = picture_one.size

#Loading pixels
pixels_cat = picture_one.load()
pixels_forest = picture_two.load()

new_picture = Image.new('RGB', picture_one.size)
new_buffer_pixels = new_picture.load()

line = 0
column = 0

for column in range (0, cat_small_width):
    for line in range (0, cat_small_height):
        r, g, b = pixels_cat [column, line]
        print(f'({column}, {line})')
        if r<100 and g == 207 and b < 100:
            new_buffer_pixels[column, line] = pixels_forest
        else:
            print(f'r: {r} g: {g} b: {b}')
            new_buffer_pixels[column, line] = pixels_cat
new_picture.show()

