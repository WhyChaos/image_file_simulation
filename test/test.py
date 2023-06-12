import numpy as np
from PIL import Image, ImageDraw
import math


def apply_curve(image_path):

    image = Image.open(image_path)
    width = image.width
    height = image.height

    curve_x = np.linspace(1, 5, width)
    curve_y = np.sin(curve_x) / curve_x * height / 50

    print(curve_x[:10])
    print(curve_y[:10])

    new_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(new_image)

    for i, x in enumerate(range(width)):
        for y in range(height):
            offset_y = math.ceil(curve_y[i]) + y
            if offset_y >= 0 and offset_y < height:
                pixel = image.getpixel((x, offset_y))
            else:
                pixel = (255, 255, 255)
            draw.point((x, y), pixel)

    new_image.save('tmp.jpg', 'JPEG')


image_path = '3.jpg'
apply_curve(image_path)
