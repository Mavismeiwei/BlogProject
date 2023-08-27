# PIL: pip install pillow

from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO

# random color of the image code
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# the char of code
str_all = string.digits + string.ascii_letters

# parameters: size, the number of digits of code, the number of points, the number of lines
def random_code(size=(200, 40), length=4, point_num=80, line_num=15):
    width, height = size

    # generate a 200*40 background img
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    draw = ImageDraw.Draw(img) # generate a draw on the img

    # configure the font style, create a font object
    font = ImageFont.truetype(font='static/resources/font/ImageCode.otf', size=32)

    # start position: (10,10); content; color
    # random choose the code
    valid_code = ''
    for i in range(length):
        random_char = random.choice(str_all)
        draw.text((40*i + 20, 10), random_char, (0, 0, 0), font=font)
        valid_code += random_char
    print(valid_code)

    # image code confusion, draw some points, lines
    # generate random points
    for i in range(point_num):
        x, y = random.randint(0, width), random.randint(0, height)  # the position of the points
        draw.point((x,y), random_color())

    # generate random lines
    for i in range(line_num):
        # start and end point position of the lines
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=random_color())

    # create a memory-based GB
    f = BytesIO()
    img.save(f, 'PNG')  # save the img in the memory-based GB
    # read the data
    data = f.getvalue()
    return (data, valid_code)


if __name__ == '__main__':
    random_code()