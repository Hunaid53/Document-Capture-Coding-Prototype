# Document-Capture-Coding-Prototype

This project is a document capture application designed to extract key information from important documents such as driver's licenses. The application utilizes Optical Character Recognition (OCR) technology to extract details like the name, document number, and expiration date from uploaded images.

## Features

- **Data Extraction**: Extracts the following details from the uploaded document:
  - Name
  - Document Number
  - Expiration Date
- **Technologies Used**:
  - Backend: Python with Flask
  - Frontend: ReactJS
  - OCR: Tesseract for text extraction from images
- **Basic Validation**: Ensures that uploaded files are in the correct format.

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm
- Tesseract OCR installed on your machine

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/document-capture-prototype.git
   cd document-capture-prototype/backend
   ```
   
2. Create a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. Install the required Python packages:
  ```bash
  pip install Flask flask-cors pytesseract Pillow opencv-python numpy
  ```

4. Ensure Tesseract is installed and set up correctly:
   - Update the path to Tesseract in your code as necessary.

### Backend Setup
1. Navigate to the frontend directory:
  ```bash
  cd ../frontend
  ```

2. Install the required Node.js packages:
  ```bash
  npm install axios
  ```

## Running the Application

### Start the Backend Server
1. Navigate to the backend directory:
  ```bash
  cd backend
  ```

2. Run the Flask application:
  ```bash
  python app.py
  ```

### Start the Frontend Application
1. Open another terminal window and navigate to the frontend directory:
  ```bash
  cd frontend
  ```

2. Start the React application:
  ```bash
  npm run dev
  ```
3. Open your web browser and navigate to http://localhost:5000 to access the application.

## Usage
1. Upload an image of a driver's license using the file input.
2. Click on "Extract Data" to retrieve key information from the document.
3. The extracted data will be displayed below the upload form.

## Sample Documents
For testing purposes, you can use these sample documents:
 - Sample Driver's License (Use DigiLocker Image)

## Contributing
Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions for Use

1. **Replace Placeholder Text**: Make sure to replace `yourusername` in the GitHub clone URL with your actual GitHub username.
2. **Add License File**: If you have a license for your project, ensure you include it in your repository.
3. **Update Paths**: If your directory structure differs, adjust paths accordingly in the README.

This README provides clear instructions for users who want to set up and run your document capture prototype while also giving an overview of its functionality and features.
