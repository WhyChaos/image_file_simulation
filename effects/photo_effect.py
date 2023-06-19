
import cv2
import numpy as np
from PIL import Image


class PhotoEffect:
    def __init__(self):
        self.background_path = 'effects/background/background.jpg'

    def main(self, image):
        # 将Pillow的Image对象转换为NumPy数组
        image_array = np.array(image)
        # # 将NumPy数组从RGB模式转换为BGR模式
        # bgr_image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
        # 将NumPy数组转换为OpenCV的图像对象
        image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

        cv2.imwrite('x.jpg', image)

        height, width, _ = image.shape

        # 加载背景图像
        background = cv2.imread(self.background_path)

        # 定义透视变换的四个点
        pts1 = np.float32([[0, 0], [image.shape[1], 0], [
            image.shape[1], image.shape[0]], [0, image.shape[0]]])
        # 定义目标图像的四个点
        pts2 = np.float32([[100, 100], [background.shape[1], 0],
                           [background.shape[1]-100, background.shape[0]-10], [0, background.shape[0]]])

        # 计算透视变换矩阵
        M = cv2.getPerspectiveTransform(pts1, pts2)

        # 执行透视变换
        transformed_image = cv2.warpPerspective(
            image, M, (background.shape[1], background.shape[0]), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

        # 将背景图像与透视变换后的图像相结合
        result = cv2.bitwise_and(background, transformed_image)

        cv2.imwrite('y.jpg', result)

        # 将OpenCV图像对象转换为RGB模式
        rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        # 创建Pillow的Image对象
        result = Image.fromarray(rgb_image)

        result.save("z.jpg", "JPEG")
        return result
