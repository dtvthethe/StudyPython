from PIL import Image
import os


def create_X_shape_image(str_img_file_name, tuple_color, size):
    im = Image.new('RGB', size, (255, 255, 255))
    for i in range(im.height):
        for j in range(im.width):
            if j in [i, im.height - i - 1]:
                im.putpixel((i, j), tuple_color)
    im.save(str_img_file_name, 'PNG')
    im.close()


def count_by_color(str_img_file_name, tuple_color):
    count = 0
    im = Image.open(str_img_file_name)
    for i in range(im.height):
        for j in range(im.width):
            if im.getpixel((i, j)) == tuple_color:
                count += 1
    return count


# Config:
str_img_file_name = 'image_output.png'
tuple_color_red = (255, 0, 0)
size = (8, 8)
img_path = os.path.join(os.getcwd(), str_img_file_name)

# Main:
if not os.path.exists(img_path):
    create_X_shape_image(str_img_file_name, tuple_color_red, size)

print('Số lượng ô màu đỏ trong hình là = %d' % (count_by_color(str_img_file_name, tuple_color_red)))
