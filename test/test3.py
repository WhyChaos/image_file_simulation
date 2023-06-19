import cv2
import numpy as np


def perspective_transform(image_path, output_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 定义透视变换前后的四个点坐标
    # 透视变换前的四个点坐标，顺序为左上、右上、右下、左下
    pts_before = np.float32([[0, 0], [image.shape[1], 0], [
                            image.shape[1], image.shape[0]], [0, image.shape[0]]])

    # 透视变换后的四个点坐标，可以根据需要进行调整
    pts_after = np.float32([[100, 100], [image.shape[1] - 200, 100],
                           [image.shape[1] - 100, image.shape[0] - 100], [100, image.shape[0] - 100]])

    # 计算透视变换矩阵
    M = cv2.getPerspectiveTransform(pts_before, pts_after)

    # 进行透视变换
    transformed_image = cv2.warpPerspective(
        image, M, (image.shape[1], image.shape[0]))

    # 将背景设置为透明，假设图像为BGR格式
    b, g, r = cv2.split(transformed_image)
    alpha = np.ones(b.shape, dtype=b.dtype) * 255
    transformed_image = cv2.merge((b, g, r, alpha))

    # 保存图像
    cv2.imwrite(output_path, transformed_image)


# 示例用法
input_image_path = "3.jpg"  # 输入图像路径
output_image_path = "output.png"  # 输出图像路径

perspective_transform(input_image_path, output_image_path)
