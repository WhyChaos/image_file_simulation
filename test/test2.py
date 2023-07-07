import cv2
import numpy as np

# 读取图像和掩码
image = cv2.imread('3.jpg')
mask = cv2.imread('moier3.jpg', 0)  # 以灰度模式读取掩码

# 对图像应用掩码
result = cv2.bitwise_and(image, image, mask=mask)

# 显示结果
cv2.imwrite('result.jpg', result)
