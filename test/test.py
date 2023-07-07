from PIL import Image, ImageDraw
import cv2


def add_moire_pattern(image_path, scale=20):
    # 打开图像
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    moier = cv2.imread('moier3.jpg')
    moier = cv2.resize(moier, (width, height))

    result = cv2.bitwise_and(image, moier)

    cv2.imwrite('result.jpg', result)


# 使用示例
add_moire_pattern('3.jpg')
