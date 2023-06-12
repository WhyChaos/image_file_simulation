from PIL import Image, ImageDraw
import random


def apply_scan_skew_effect(image_path, probability=0.01):
    # 打开图像
    image = Image.open(image_path)

    # 创建新的图像，与原图像大小相同
    new_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(new_image)

    width, height = image.size

    # 遍历每个扫描线
    for y in range(0, height):
        # 是否为扫描线
        scan_line = random.random() < probability

        # 绘制偏斜后的扫描线
        for x in range(width):
            if scan_line:
                # 白扫描线和黑扫描线概率各50%
                if random.random() < 0.5:
                    pixel = (255, 255, 255)
                else:
                    pixel = (0, 0, 0)
            else:
                pixel = image.getpixel((x, y))

            # 在新图像上绘制像素
            draw.point((x, y), pixel)

    # 保存处理后的图像
    new_image.save("scanned_image.jpg")


# 调用函数并传入图像路径
apply_scan_skew_effect("3.jpg")
