import cv2
import numpy as np

def apply_scan_effect(image):
    # 调整图像大小以模拟扫描效果
    resized = cv2.resize(image, None, fx=0.5, fy=0.5)
    
    # 将图像转换为灰度
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    # 应用高斯模糊以模拟扫描效果
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 使用大津阈值化方法进行二值化
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 返回扫描效果的图像
    return threshold

def apply_photograph_effect(image):
    # 添加高斯噪声
    noisy_image = np.float32(image) + np.random.randn(*image.shape) * 15
    
    # 将图像转换为8位无符号整型
    noisy_image = np.uint8(np.clip(noisy_image, 0, 255))
    
    # 应用高斯模糊
    blurred_image = cv2.GaussianBlur(noisy_image, (15, 15), 0)
    
    # 返回拍照后的效果图像
    return blurred_image

# 读取输入图像
input_image = cv2.imread('2.jpg')

# 应用扫描效果
# output_image = apply_photograph_effect(input_image)

# 显示原始图像和处理后的图像
# cv2.imshow('Original Image', input_image)
# cv2.imshow('Scan Effect', output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('tmp.jpg',input_image )
