from PIL import ImageEnhance, Image

# 打开图像
image = Image.open("1.jpg")

# 创建对比度增强器
contrast_enhancer = ImageEnhance.Contrast(image)

# 增强对比度，参数大于1增强对比度，小于1降低对比度
contrast_factor = 1.5
image = contrast_enhancer.enhance(contrast_factor)

# 创建亮度增强器
brightness_enhancer = ImageEnhance.Brightness(image)

# 增强亮度，参数大于1增强亮度，小于1降低亮度
brightness_factor = 1.2
image = brightness_enhancer.enhance(brightness_factor)

# 保存修改后的图像
image.save("modified_image.jpg")
