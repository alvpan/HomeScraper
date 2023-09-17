import pytesseract
from PIL import Image

#These should be adjustable on setup too
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
input_image = 'image.png'

#use tesseract to extract text from image
try:
    image = Image.open(input_image)
    text = pytesseract.image_to_string(image)
    with open('text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    print(f'OCR done. Text saved to "text.txt".')
except Exception as e:
    print(f'OCR ERROR!: {e}')
