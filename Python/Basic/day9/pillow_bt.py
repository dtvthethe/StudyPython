from PIL import Image
#tao hinh o co
img = Image.new('RGB', (8,8), (0,255,255))
img.show()
img.save('bt_create_image.png', 'PNG')
img.close()

img = Image.new('RGB', (8,8),(255,255,255))
for i in range(0,8):
    for j in range(0,8):
        if i%2 == j%2: img.putpixel((i,j),(255,0,0))
img.save('trang_do.png', 'PNG')
img.show()
img.close()
#red count pixel





#resize image




#rotate 45do


#crop image


#gaus