
import cv2
import numpy as np
from PIL import Image
import random


class PhotoEffect:
    def __init__(self):
        # 背景图，四个坐标：左上，右上，右下，左下
        self.coordinate = [
            {
                'filename': 'background1.jpg',
                'coordinate': [[122, 122], [651, 134], [815, 926], [-30, 918]]
            },
            {
                'filename': 'background2.jpg',
                'coordinate': [[306, 133], [1099, 214], [1300, 1384], [283, 1471]]
            },
            {
                'filename': 'background3.jpg',
                'coordinate': [[163, 127], [979, 173], [1197, 1358], [153, 1456]]
            },
            {
                'filename': 'background4.jpg',
                'coordinate': [[291, 171], [1078, 258], [1120, 1376], [259, 1419]]
            },
            {
                'filename': 'background5.jpg',
                'coordinate': [[224, 149], [970, 122], [1174, 1219], [147, 1272]]
            },
            {
                'filename': 'background6.jpg',
                'coordinate': [[129, 467], [398, -15], [1169, 355], [832, 897]]
            },
            {
                'filename': 'background7.jpg',
                'coordinate': [[105, 381], [117, 94], [536, 100], [538, 392]]
            },
            {
                'filename': 'background8.jpg',
                'coordinate': [[114, 487], [107, 104], [663, 92], [677, 481]]
            },
            {
                'filename': 'moier4.jpg',
                'coordinate': [[466, 177], [1216, 175], [1206, 1194], [502, 1218]]
            },
            {
                'filename': 'moier5.jpg',
                'coordinate': [[318, 267], [907, 330], [884, 1081], [317, 1159]]
            }
        ]
        self.background_path = 'effects/background/'

    def main(self, image):
        # 将Pillow的Image对象转换为NumPy数组
        image_array = np.array(image)
        # # 将NumPy数组从RGB模式转换为BGR模式
        # bgr_image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
        # 将NumPy数组转换为OpenCV的图像对象
        image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

        height, width, _ = image.shape

        # background_index = random.randint(0, len(self.coordinate)-1)
        background_index = 9

        # 加载背景图像
        background = cv2.imread(self.background_path +
                                self.coordinate[background_index]['filename'])

        # 定义透视变换的四个点
        pts1 = np.float32([[0, 0], [image.shape[1], 0], [
            image.shape[1], image.shape[0]], [0, image.shape[0]]])
        # 定义目标图像的四个点
        pts2 = np.float32(self.coordinate[background_index]['coordinate'])

        # 计算透视变换矩阵
        M = cv2.getPerspectiveTransform(pts1, pts2)

        # 执行透视变换
        transformed_image = cv2.warpPerspective(
            image, M, (background.shape[1], background.shape[0]), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

        # 将背景图像与透视变换后的图像相结合
        result = cv2.bitwise_and(background, transformed_image)

        # 将OpenCV图像对象转换为RGB模式
        rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        # 创建Pillow的Image对象
        result = Image.fromarray(rgb_image)

        return result
