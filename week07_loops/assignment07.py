#Assignment Week 07 - Milestone
#From: https://byui-cse.github.io/cse110-course/lesson07/prove.html
#By: Felipe dos Santos Belisário



from PIL import Image


image_desert = Image.open('desert.jpg')



print(image_desert.size)
print(image_desert.format)

pixels_desert = image_desert.load()

print(pixels_desert[201, 100])
print(pixels_desert[202, 100])
print(pixels_desert[203, 100])
print(pixels_desert[204, 100])
print(pixels_desert[205, 100])

pixels_desert[201, 100] = (255, 0, 0)
pixels_desert[202, 100] = (255, 0, 0)
pixels_desert[203, 100] = (255, 0, 0)
pixels_desert[204, 100] = (255, 0, 0)
pixels_desert[205, 100] = (255, 0, 0)

image_desert.save('desert.jpg')
image_desert.show()