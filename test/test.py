import paddleocr
from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang="ch")
image_path = '3.jpg'  # 替换为你的图像路径
image = cv2.imread(image_path)  # 使用OpenCV加载图像
result = ocr.ocr(image, cls=True)  # 进行OCR识别
for line in result:
    print(line)
    print('======')
    for word in line:
        text = word[1][0]  # 获取识别文本

        print(text)
        print('-----')
        if "中国" in text:  # 替换 "关键字" 为你要打码的具体关键字
            print('包含中国')
            bbox = word[0]  # 获取关键字所在的坐标信息
            xmin, ymin, xmax, ymax = bbox
            image = cv2.rectangle(
                image, (xmin, ymin), (xmax, ymax), (0, 0, 0), -1)  # 在图像上绘制黑色矩形框进行打码

# 或者保存结果图像
cv2.imwrite("result.jpg", image)
