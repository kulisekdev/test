from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

# Windows users: Set Tesseract path (uncomment if needed)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']  # Get the uploaded image
    img = Image.open(io.BytesIO(image.read()))  # Convert to PIL Image

    extracted_text = pytesseract.image_to_string(img)  # Extract text using Tesseract
    return jsonify({"extracted_text": extracted_text})  # Return response

if __name__ == '__main__':
    app.run(debug=True)
