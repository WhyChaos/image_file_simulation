from pdf2image import convert_from_path
import os


class pdf2image:

    @staticmethod
    def pdf_to_images(pdf_path, output_folder):
        images = convert_from_path(pdf_path)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        for i, image in enumerate(images):
            image_path = f"{output_folder}/page_{i + 1}.jpg"
            image.save(image_path, 'JPEG')
            print(type(image))
            print(f"Page {i + 1} saved as {image_path}")

# 使用示例
pdf_path = '1.pdf'
output_folder = 'pdf'

pdf_to_images(pdf_path, output_folder)
