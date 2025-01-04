

# Resume Parser API

A Flask-based web application that provides an API for parsing resumes and extracting useful information using the `pyresparser` library.

## Features

- Parses resumes in PDF format to extract key details such as name, email, phone, skills, experience, education, etc.
- Provides a simple API endpoint for uploading and processing resumes.
- Includes a health check endpoint to verify the application's status.

---

## Requirements

- Python 3.7 or later
- Virtual Environment (optional but recommended)
- Libraries specified in the `requirements.txt` file

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/resume-parser-api.git
   cd resume-parser-api
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK stopwords:

   ```python
   python -c "import nltk; nltk.download('stopwords')"
   ```

---

## Usage

1. Start the application:

   ```bash
   python app.py
   ```

   The application will run on `http://0.0.0.0:8030`.

2. Test the health check endpoint:

   ```bash
   curl http://localhost:8030/ping
   ```

3. Parse a resume:

   - Use a tool like Postman or `curl` to send a POST request to `/resume-parser` with a resume file.

   ```bash
   curl -X POST -F "resume=@path/to/resume.pdf" http://localhost:8030/resume-parser
   ```

   - Replace `path/to/resume.pdf` with the actual file path of your resume.

---

## API Endpoints

### 1. Health Check
- **Endpoint:** `/ping`
- **Method:** `GET`
- **Response:**  
  ```json
  {
      "status": "Healthy"
  }
  ```

### 2. Resume Parsing
- **Endpoint:** `/resume-parser`
- **Method:** `POST`
- **Parameters:**  
  - `resume`: A PDF file of the resume.
- **Response:** Extracted data in JSON format.  
  Example:  
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "1234567890",
      "skills": ["Python", "Flask", "Machine Learning"],
      ...
  }
  ```

---

## Logging

The application uses Python's `logging` module to log debugging information and errors to the console.

---

## Warning Handling

Warnings are suppressed to avoid unnecessary clutter in the output. This can be adjusted by modifying the `warnings.filterwarnings` setting in the code.

---

## Deployment

This application can be deployed using platforms like Heroku, AWS, Google Cloud, or any containerized service like Docker.

---

## Contributing

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes and push.
4. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

[Badal Gupta](https://github.com/<your-username>)  
Feel free to connect for questions or collaborations!
