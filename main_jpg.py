
from PIL import Image

from ocr.paddleocr import OCR
from erase.index import erase
from judge.index import Judge
from effects.index import Effect

import os
import glob

orc = OCR.main


def main():
    for infile in glob.glob("./input/*.jpg"):
        infile = os.path.abspath(infile)
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as img:
            coordinate_word_list = orc(infile)
            print(infile)
            print(coordinate_word_list)

            coordinate_list = []
            for coordinate_word in coordinate_word_list:
                if (Judge.main(coordinate_word['word'])):
                    print(coordinate_word['word'])
                    coordinate_list.append(coordinate_word['coordinate'])

            img = erase(img=img, coordinate_list=coordinate_list)

            img = Effect.apply_scan_effect(img)

            img.save('./output/' + file.split('/')[-1] + ".jpg", "JPEG")


if __name__ == '__main__':

    main()
