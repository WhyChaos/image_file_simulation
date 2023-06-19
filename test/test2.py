import cv2
import numpy as np


def replace_background(image_path, background_path, output_path):
    # 加载原始图像
    image = cv2.imread(image_path)
    print(type(image))
    height, width, _ = image.shape

    # 加载背景图像
    background = cv2.imread(background_path)

    # 定义透视变换的四个点
    pts1 = np.float32([[0, 0], [image.shape[1], 0], [
        image.shape[1], image.shape[0]], [0, image.shape[0]]])
    # 定义目标图像的四个点
    pts2 = np.float32([[0, 100], [background.shape[1], 0],
                       [background.shape[1]-100, background.shape[0]-10], [0, background.shape[0]]])

    # 计算透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # 执行透视变换
    transformed_image = cv2.warpPerspective(
        image, M, (background.shape[1], background.shape[0]), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    # 将背景图像与透视变换后的图像相结合
    result = cv2.bitwise_and(background, transformed_image)

    # 保存结果图像
    cv2.imwrite(output_path, result)


# 使用示例
image_path = '3.jpg'
background_path = 'background.jpg'
output_path = 'output.jpg'

replace_background(image_path, background_path, output_path)
