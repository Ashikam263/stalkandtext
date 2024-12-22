# from gettext import install
# import pytesseract # type: ignore
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


# pip install pytesseract
# pip install pillow


from PIL import Image
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
img = Image.open(r'C:\Users\ashik\Downloads\ilovepdf_pages-to-jpg\22qpcomputer programmer_page-0012.jpg')


# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
