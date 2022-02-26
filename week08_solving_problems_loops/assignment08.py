#Assignment Week 08 - Solving Problems Using Loops
#From: https://byui-cse.github.io/cse110-course/lesson07/prove.html
#By: Felipe dos Santos Belisário


from PIL import Image
print('\n****************************************************')
print('\n*            WELCOME TO THE PIXEL FUN!!!             *')
print('\n****************************************************')

#Load a green image.
while True:
    picture_one = input('\nPlease, select your item image. Type: BOAT, CACTUS, CAT, CAT_SMALL, HARVESTER, HIKER, PENGUIN or SPACESHUTTLE: ').lower()
    if picture_one == 'boat':
        picture_one = Image.open('./boat.jpg')
        break
    elif picture_one == 'cactus':
        picture_one = Image.open('./cactus.jpg')
        break
    elif picture_one == 'cat':
        picture_one = Image.open('./cat.jpg')
        break
    elif picture_one == 'cat_small':
        picture_one = Image.open('./cat_small.jpg')
        break
    elif picture_one == 'harvester':
        picture_one = Image.open('./harvester.jpg')
        break
    elif picture_one == 'hiker':
        picture_one = Image.open('./hiker.jpg')
        break
    elif picture_one == 'penguin':
        picture_one = Image.open('./penguin.jpg')
        break
    elif picture_one == 'spaceshuttle':
        picture_one = Image.open('./spaceshuttle.jpg')
        break
    else:
        print('\nPicture Invalid. Please try again')
#Load Background image
while True:
    picture_two = input('\nPlease, select your background image. Type: BEACH, DESERT, EARTH, FIELD, FOREST, SNOWSCAPE or SUNSET: ').lower()
    if picture_two == 'beach':
        picture_two = Image.open('./beach.jpg')
        break
    elif picture_two == 'desert':
        picture_two = Image.open('./desert.jpg')
        break
    elif picture_two == 'earth':
        picture_two = Image.open('./earth.jpg')
        break
    elif picture_two == 'field':
        picture_two = Image.open('./field.jpg')
        break
    elif picture_two == 'forest':
        picture_two = Image.open('./forest.jpg')
        break
    elif picture_two == 'snowscape':
        picture_two = Image.open('./snowscape.jpg')
        break
    elif picture_two == 'sunset':
        picture_two = Image.open('./sunset.jpg')
        break
    else:
        print('\nPicture Invalid. Please try again')


#Pick-up the Image sizes
item_width, item_height = picture_one.size

#Loading pixels
pixels_item = picture_one.load()
pixels_background = picture_two.load()

#Create a new image that is the same size as the other images.
new_picture = Image.new('RGB', picture_one.size)
new_picture_pixels = new_picture.load()


#Iterate through all the pixels of the green image. Check to see if the green value is greater than a certain number and that the red and blue values are less than a certain number. If so, get the red, green, and blue values from the pixel at that location in the background image, if it's not a bright green color, get the red, green, and blue values from the pixel at that location in the green, foreground image.

for column in range (0, item_width):
    for line in range (0, item_height):
        (r, g, b) = pixels_item [column, line]
        (br, bg, bb) = pixels_background[column, line]
        # print(f'({column}, {line})')
        #Set the pixel in your new image to have the appropriate red, green, and blue value, as described.
        if (r <100 and g > 180 and b < 100):
            new_picture_pixels[column, line] = (br, bg, bb)
        else:
            # print(f'r: {r} g: {g} b: {b}') 
            new_picture_pixels[column, line] = (r, g, b)
print('\n Saving image, please wait....\n')            
#Save the new image to a file.
new_picture.save('new_picture.jpg')



