import pytesseract
from PIL import Image
import math


def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False


# 打开图像文件
image = Image.open('1.jpg')

# 使用Tesseract进行OCR
# text = pytesseract.image_to_string(
#     image, lang='chi_sim', config='--tessdata-dir "/home/hc/pic/tessdata"')
# print(text)


result = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT,
                                   lang='chi_sim', config='--tessdata-dir "/home/hc/pic/tessdata" ')
# 提取每个单词的位置信息
word_boxes = []
words = []
for i, word in enumerate(result['text']):
    if word.strip() != '':
        left = result['left'][i]
        top = result['top'][i]
        width = result['width'][i]
        height = result['height'][i]

        # 存储单词的位置信息
        word_box = (left, top, left + width, top + height)
        word_boxes.append(word_box)
        words.append(word)

# 根据单词的位置信息，合并相邻的单词形成句子的位置信息
sentence_boxes = []
sentences = []

current_sentence = ''
current_sentence_box = (0, 0, 0, 0)
for word, word_box in zip(words, word_boxes):
    if len(current_sentence) == 0:
        current_sentence = word
        current_sentence_box = word_box
    else:
        # 判断当前单词是否与前一个单词在同一行
        if not is_chinese(word) or abs(word_box[1] - current_sentence_box[1]) < current_sentence_box[3]-current_sentence_box[1]:
            current_sentence += word
            current_sentence_box = (min(current_sentence_box[0], word_box[0]),
                                    min(current_sentence_box[1], word_box[1]),
                                    max(current_sentence_box[2], word_box[2]),
                                    max(current_sentence_box[3], word_box[3]))
        else:
            sentence_boxes.append(current_sentence_box)
            sentences.append(current_sentence)

            current_sentence = word
            current_sentence_box = word_box

# 存储最后一个句子的位置信息
if len(current_sentence) > 0:
    sentence_boxes.append(current_sentence_box)
    sentences.append(current_sentence)

# 打印每句话的位置信息
for sentence, sentence_box in zip(sentences, sentence_boxes):
    print(f'{sentence} Position: {sentence_box}')
