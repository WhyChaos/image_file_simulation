
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import random
import numpy as np
import math


class ScanEffect:
    def main(self, image):
        # 蜷曲
        image = self.apply_scan_curve_effect(image)
        # 扫描线
        image = self.apply_scan_line_effect(image)
        # 噪点
        image = self.apply_scan_noise_effect(image)

        # 转换为灰度图像
        # image = image.convert('L')

        # # 应用中值滤波以去除噪点
        # image = image.filter(
        #     ImageFilter.MedianFilter(size=3))

        # # 增强对比度
        # enhancer = ImageEnhance.Contrast(image)
        # image = enhancer.enhance(2.0)

        # # 应用边缘增强滤波器
        # image = image.filter(
        #     ImageFilter.EDGE_ENHANCE_MORE)

        return image

    def apply_scan_line_effect(self, image, probability=0.01):
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

        return new_image

    def apply_scan_noise_effect(self, image, probability=0.001):
        # 创建新的图像，与原图像大小相同
        new_image = Image.new("RGB", image.size)
        draw = ImageDraw.Draw(new_image)
        width, height = image.size
        # 遍历
        for y in range(0, height):
            for x in range(width):
                scan_noise = random.random() < probability
                if scan_noise:
                    # 白和黑概率各50%
                    if random.random() < 0.5:
                        pixel = (255, 255, 255)
                    else:
                        pixel = (0, 0, 0)
                else:
                    pixel = image.getpixel((x, y))

                # 在新图像上绘制像素
                draw.point((x, y), pixel)

        return new_image

    def apply_scan_curve_effect(self, image):
        width = image.width
        height = image.height
        curve_x = np.linspace(1, 5, width)
        curve_y = np.sin(curve_x) / curve_x * height / 50
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

        return new_image
