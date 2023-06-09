
from PIL import Image

from ocr.tesseract import OCR
from erase.index import erase
from judge.index import Judge
from effects.index import Effect

import os
import glob


def main():
    for infile in glob.glob("./input/*.jpg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as img:
            coordinate_word_list = OCR.by_row(infile)
            print(coordinate_word_list)

            coordinate_list = []
            for coordinate_word in coordinate_word_list:
                if (Judge.main(coordinate_word['word'])):
                    coordinate_list.append(coordinate_word['coordinate'])

            img = erase(img=img, coordinate_list=coordinate_list)

            img = Effect.apply_scan_effect(img)

            img.save('./output/' + file.split('/')[-1] + ".jpg", "JPEG")


if __name__ == '__main__':

    main()
