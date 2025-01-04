import os
import nltk
import logging
import tempfile
nltk.download('stopwords')
from flask import Flask, request, jsonify
from pyresparser import ResumeParser
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# Initialize Flask app
app = Flask(__name__)

# API Endpoint for Resume Parsing
@app.route('/resume-parser', methods=['POST'])
def resume_parser():
    try:
        # Check if the file is included in the request
        if 'resume' not in request.files:
            return jsonify({'error': 'No file provided. Please upload a resume PDF.'}), 400
        
        file = request.files['resume']
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)

        # Parse the resume and extract data
        data = ResumeParser(file_path).get_extracted_data()
        os.remove(file_path)  # Clean up temporary file
        
        # Return extracted data as JSON
        return jsonify(data), 200

    except Exception as e:
        logger.error(f"Error during resume parsing: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'Healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8030)
