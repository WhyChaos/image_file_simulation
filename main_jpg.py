
from PIL import Image

from ocr.paddleocr import OCR
from erase.index import erase
from judge.index import Judge
from effects.index import Effect

import os
import glob

# ocr，使用paddleocr
orc = OCR.main
# 关键字判断
judge = Judge(keyword_path='./judge/keyword.dic', by_row=False)
# 定义特效，扫描或拍照 type='photo'|type='scan'|type='photo_screen'|type='screen'
effect = Effect(type='screen')


def main():
    # 遍历所有jpg文件
    for infile in glob.glob("./input/*.jpg"):
        infile = os.path.abspath(infile)
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as img:
            # 通过ocr获得文字内容和位置新分析
            coordinate_word_list = orc(infile)
            print(infile)
            print(coordinate_word_list)

            # coordinate_list = []
            # for coordinate_word in coordinate_word_list:
            #     # 判断是否为关键字
            #     if (judge.main(coordinate_word['word'])):
            #         print(coordinate_word['word'])
            #         coordinate_list.append(coordinate_word['coordinate'])

            coordinate_list = judge.main(coordinate_word_list)

            # 抹去关键字信息，马赛克或全黑效果 type='dark'|type='mosaic'
            img = erase(img=img, coordinate_list=coordinate_list)
            # img = erase(img=img, coordinate_list=coordinate_list, type='dark')

            # 模拟特效，扫描或拍照
            img = effect.main(img)

            img.save('./output/' + file.split('/')[-1]+".jpg", "JPEG")


if __name__ == '__main__':
    main()
