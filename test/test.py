import cv2
import numpy as np

# 读取原始文档图片
image = cv2.imread('3.jpg')

# 定义原始文档的四个角点
original_corners = np.float32([[0, 0], [image.shape[1], 0], [
                              image.shape[1], image.shape[0]], [0, image.shape[0]]])

# 定义目标文档的四个角点（模拟拍照的角度）
# 调整下面的坐标值来改变角度
target_corners = np.float32([[100, 100], [image.shape[1]-10, 200],
                            [image.shape[1]-20, image.shape[0]-10], [200, image.shape[0]-20]])

# 计算透视变换矩阵
perspective_matrix = cv2.getPerspectiveTransform(
    original_corners, target_corners)

# 进行透视变换
result = cv2.warpPerspective(
    image, perspective_matrix, (image.shape[1], image.shape[0]), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))


cv2.imwrite('output.jpg', result)
