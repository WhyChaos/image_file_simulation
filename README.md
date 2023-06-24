### 总体介绍
执行下面代码，遍历input文件夹中的jpg文件，输出到output文件
```
python main_jpg.py
```
执行下面代码，遍历input文件夹中的pdf文件，输出到output文件
```
python main_pdf.py
```

### 文件/文件夹介绍
***requirement.txt*** python依赖包
***test/*** 开发用于测试
***effect/*** 特效，目前有模拟扫描和拍照的，其中background/存放拍照模拟拍照效果时的背景图
***erase/*** 抹去关键字，目前有马赛克和全黑
***input/*** 存放输入的文件
***output/*** 存放输出的文件
***judge/*** 判断是否文关键字，其中keyword.dic存放关键字，每个关键字空格隔开
***ocr/*** 对图像进行ocr，目前有调用阿里api、tesseract、paddleocr，由于paddleocr最快最准，现在只是用paddleocr
***pdf_to_image/*** 将pdf转换为图片（jpg）
~~***tessdata/*** 使用tesseract进行ocr时，对简体中文的识别包，现在不需要~~ 

