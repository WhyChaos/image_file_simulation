from PIL import Image, ImageFilter, ImageEnhance


# 打开原始图像
image = Image.open('3.jpg')

# 转换为灰度图像
grayscale_image = image.convert('L')

# 应用中值滤波以去除噪点
filtered_image = grayscale_image.filter(ImageFilter.MedianFilter(size=3))

# 增强对比度
enhancer = ImageEnhance.Contrast(filtered_image)
enhanced_image = enhancer.enhance(2.0)

# 应用边缘增强滤波器
edge_enhanced_image = enhanced_image.filter(ImageFilter.EDGE_ENHANCE_MORE)

# 保存扫描效果图像
edge_enhanced_image.save('tmp.jpg')

