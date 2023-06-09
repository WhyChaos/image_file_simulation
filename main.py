
from PIL import Image

from ocr.index import Sample
from erase.index import erase
from judge.index import Judge

import os, glob



def main():
    for infile in glob.glob("./input/*.jpg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as img:
            coordinate_word_list = Sample.main(infile)
            coordinate_list = []
            for coordinate_word in coordinate_word_list:
                if(Judge.main(coordinate_word['word'])):
                    coordinate_list.append(coordinate_word['coordinate'])
            img = erase(img=img, coordinate_list=coordinate_list)
            img.save('./output/' + file.split('/')[-1]+ ".jpg", "JPEG")

if __name__ == '__main__':

    main()
