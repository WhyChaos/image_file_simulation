from pdf2image import convert_from_path
import os

output_folder = 'pdf'


class pdf_to_image:

    @staticmethod
    def main(pdf_path):

        images = convert_from_path(pdf_path)

        return images

        # for i, image in enumerate(images):
        #     image_path = f"{output_folder}/page_{i + 1}.jpg"
        #     image.save(image_path, 'JPEG')
        #     print(type(image))
        #     print(f"Page {i + 1} saved as {image_path}")
