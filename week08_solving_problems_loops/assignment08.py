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
