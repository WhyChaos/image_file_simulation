# 环境安装
创建虚拟环境
```
conda create --name pic python=3.8
```
安装python依赖
```
pip install -r requirements.txt
```
# 总体介绍

执行下面代码，遍历 input 文件夹中的 jpg 文件，输出到 output 文件

```
python main_jpg.py
```

执行下面代码，遍历 input 文件夹中的 pdf 文件，输出到 output 文件

```
python main_pdf.py
```

# 文件/文件夹介绍

**_requirement.txt_** python 依赖包

**_test/_** 开发用于测试

**_effect/_** 特效，目前有模拟扫描和拍照的，其中 background/存放拍照模拟拍照效果时的背景图

**_erase/_** 抹去关键字，目前有马赛克和全黑

**_input/_** 存放输入的文件

**_output/_** 存放输出的文件

**_judge/_** 判断是否文关键字，其中 keyword.dic 存放关键字，每个关键字空格隔开

**_ocr/_** 对图像进行 ocr，目前有调用阿里 api、tesseract、paddleocr，由于 paddleocr 最快最准，现在只是用 paddleocr

**_pdf_to_image/_** 将 pdf 转换为图片（jpg）

~~**_tessdata/_** 使用 tesseract 进行 ocr 时，对简体中文的识别包，现在不需要~~

# 功能介绍
对文档（图片或pdf）进行orc，对关键字进行打码，模拟成扫描/拍照，输出图片

## ocr
使用paddleorc
## 打码
对关键字进行打码，有马赛克、全黑效果
## 模拟扫描效果
使用Pillow，按遍历像素，首先对图片根据蜷曲函数进行蜷曲，然后一定概率增加白扫描线或黑扫描线，然后一定概率增加噪点
## 模拟拍照效果
使用opencv对图像进行透视变换，然后按位与操作与背景图合并起来。

添加背景图：将背景图添加至‘./effects/background’目录下，并在‘./effects/photo_effect.py’中添加坐标。