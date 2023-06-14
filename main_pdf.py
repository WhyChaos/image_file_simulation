
from PIL import Image

from ocr.paddleocr import OCR
from erase.index import erase
from judge.index import Judge
from effects.index import Effect
from pdf_to_image.index import pdf_to_image

import os
import glob

orc = OCR.main


def main():
    for infile in glob.glob("./input/*.pdf"):
        infile = os.path.abspath(infile)
        file, ext = os.path.splitext(infile)

        output_folder = 'output/' + file.split('/')[-1]
        output_folder = os.path.abspath(output_folder)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        images = pdf_to_image.main(infile)

        for i, image in enumerate(images):
            output_file = output_folder + f'/page_{i+1}.jpg'
            image.save(output_file, 'JPEG')

            coordinate_word_list = orc(output_file)
            print(output_file)
            print(coordinate_word_list)

            coordinate_list = []
            for coordinate_word in coordinate_word_list:
                if (Judge.main(coordinate_word['word'])):
                    coordinate_list.append(coordinate_word['coordinate'])

            image = erase(img=image, coordinate_list=coordinate_list)

            image = Effect.apply_scan_effect(image)

            image.save(output_file, "JPEG")


if __name__ == '__main__':

    main()
