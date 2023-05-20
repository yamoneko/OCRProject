import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def get_text(img_name):
    image = Image.open(img_name)
    text = pytesseract.pytesseract.image_to_string(image)
    return text


output = get_text("t3.jpg")
print(output)