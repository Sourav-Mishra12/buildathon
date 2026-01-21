import pytesseract
from PIL import Image
import io

# ✅ EXACT TESSERACT PATH (CONFIRMED)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

async def extract_text(file):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image, lang="eng")
    return text
