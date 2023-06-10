import pdfplumber


def extract_text_with_position(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text_with_position = []
        for page in pdf.pages:
            for element in page.extract_words():
                text_with_position.append({
                    'text': element['text'],
                    'x0': element['x0'],
                    'x1': element['x1'],
                    'top': element['top'],
                    'bottom': element['bottom']
                })
    return text_with_position


pdf_path = '1.pdf'
text_with_position = extract_text_with_position(pdf_path)
for element in text_with_position:
    print('Text:', element['text'])
    print('Position:',
          f'x0={element["x0"]}, x1={element["x1"]}, top={element["top"]}, bottom={element["bottom"]}')
    print('---')
