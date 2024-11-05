from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import re
import cv2
import numpy as np

# Update this path if necessary based on your installation location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # For Windows



app = Flask(__name__)
CORS(app)

def preprocess_image(image_path):
    """Preprocess the image for better OCR results."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = cv2.adaptiveThreshold(blurred, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    return binary

def extract_data(image_path):
    """Extract data from the given image using OCR."""
    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image, config='--psm 6')
    print("Extracted Text:", text)

    name_pattern = r'NAME : \s*[\n\s]*([A-Za-z]+\s+[A-Z]\s+[A-Za-z]+)'
    doc_number_pattern = r'License No\.  : \s*([\w\d]+ [\w\d]+)'
    exp_date_pattern = r'(?:Expiration Date|Date of Expiry)\s*:\s*(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})'

    name = re.search(name_pattern, text)
    doc_number = re.search(doc_number_pattern, text)
    exp_date = re.search(exp_date_pattern, text)

    return {
        "name": name.group(1) if name else None,
        "document_number": doc_number.group(1) if doc_number else None,
        "expiration_date": exp_date.group(1) if exp_date else None,
    }

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    file.save("temp_image.png")
    
    extracted_data = extract_data("temp_image.png")

    return jsonify(extracted_data)

if __name__ == '__main__':
    app.run(debug=True)