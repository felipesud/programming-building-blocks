#Assignment Week 08 - Solving Problems Using Loops
#From: https://byui-cse.github.io/cse110-course/lesson07/prove.html
#By: Felipe dos Santos Belisário


from PIL import Image
#Call Images
picture_one = Image.open('./cactus.jpg')
picture_two = Image.open('./desert.jpg')


#Pick-up the Image sizes
item_small_width, item_small_height = picture_one.size

#Loading pixels
pixels_item = picture_one.load()
pixels_background = picture_two.load()

new_picture = Image.new('RGB', picture_one.size)
new_picture_pixels = new_picture.load()



for column in range (0, item_small_width):
    for line in range (0, item_small_height):
        (r, g, b) = pixels_item [column, line]
        (br, bg, bb) = pixels_background[column, line]
        # print(f'({column}, {line})')
        if (r <100 and g > 200 and b < 100):
            new_picture_pixels[column, line] = (br, bg, bb)
        else:
            # print(f'r: {r} g: {g} b: {b}') 
            new_picture_pixels[column, line] = (r, g, b)
new_picture.save('cactus_desert.jpg')

