from PIL import Image
# img = Image.new('RGB', (8,8), (0,255,0))
# # img = Image.open('1.jpg')0
# img.save('red8.png', 'PNG')
# img.show()
# img.close()



# img = Image.new('RGB', (8,8), (0,0,0))
# # img = Image.open('1.jpg')0
# for i in range(0,8):
#     for j in range(0,8):
#         if i%2 == j%2:
#             img.putpixel((i,j),(255,255,255))
# img.save('bc_den_trang.png', 'PNG')
# img.show()


img = Image.new('RGB', (10,10), (255,255,255,255))
for i in range(0,10):
    for j in range(0,10):
        if i%2 == j%2 & img.rotate(45):

            img.putpixel((i,j),(255,0,0))
img.save('cheo_trang_do.png', 'PNG')
img.show()
img.close()


# img = Image.open('bc.png')
# count = 0
# for i in range(img.height):
#     for j in range(img.width):
#         if img.getpixel((i,j)) == (255,0,0):
#             count +=1
# print(count)

# resize
# img = Image.open('1.jpg')
# print(img.width, img.height)
# img = img.resize((200, 200), Image.ANTIALIAS)
# img.save('anh_100.jpg', 'JPEG')
# img.show()
# img.close()

# img = Image.open('1.jpg')
# print(img.width, img.height)
# img = img.rotate(45)
# img = img.crop(800, 1000, 2000, 1500)
# img.show()
# img.close()

from PIL import ImageFilter
#Mo anh
# img = Image.open('1.jpg')
# img = img.filter(ImageFilter.GaussianBlur(9))
# img.save('1_mo.jpg', 'JPEG')
# img.show()
# img.close()

# #Ro anh
# img = Image.open('1_mo.jpg')
# img = img.filter(ImageFilter.UnsharpMask(radius=10, percent=500, threshold=40))
# img.show()
# img.close()








