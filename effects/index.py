
from PIL import Image, ImageFilter, ImageEnhance


class Effect:
    @staticmethod
    def apply_scan_effect(image):
        # 转换为灰度图像
        grayscale_image = image.convert('L')

        # 应用中值滤波以去除噪点
        filtered_image = grayscale_image.filter(ImageFilter.MedianFilter(size=3))

        # 增强对比度
        enhancer = ImageEnhance.Contrast(filtered_image)
        enhanced_image = enhancer.enhance(2.0)

        # 应用边缘增强滤波器
        edge_enhanced_image = enhanced_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        return edge_enhanced_image