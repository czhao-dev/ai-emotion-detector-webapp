
# AI-Based Emotion Detection Web Application

## Overview

This project is a final assignment for an AI engineering course. You will assume the role of a software engineer tasked with developing an AI-based web application capable of detecting emotions from textual input. The application leverages IBM Watson's NLP capabilities and is built using Python and Flask.

The project is divided into 8 main tasks, each contributing to a final score of 16 points. These tasks involve setting up a local development environment, creating and formatting the application, performing tests, deploying the app, and adhering to good software engineering practices.

## Features

- Accepts textual input and analyzes the emotional tone.
- Uses IBM Watson NLP library for emotion detection.
- Flask-powered web UI.
- Unit tests to ensure functionality.
- Static code analysis with pylint or flake8.
- Error handling and user-friendly messages.
- Easily deployable web app.

## Technologies Used

- Python 3.8+
- Flask
- IBM Watson NLP
- HTML/CSS (for frontend)
- Pytest or Unittest (for unit testing)
- pylint or flake8 (for code analysis)

## Project Structure

```
emotion-detector/
│
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── server.py
├── emotion_detector.py
├── test_emotion_detector.py
├── .pylintrc or .flake8
└── README.md
```

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

## Tasks Overview

### Task 1: Clone the Repository

You should clone this GitHub repository using the instructions above.

### Task 2: Create Emotion Detection App

Use IBM Watson NLP SDK to detect emotions from input text. The core functionality resides in `emotion_detector.py`.

### Task 3: Format Output

Ensure the application returns emotion data in a clean, formatted way (e.g., dictionary or JSON with emotion scores).

### Task 4: Package Application

All files should be organized and dependencies listed in `requirements.txt`.

### Task 5: Run Unit Tests

Use `unittest` or `pytest` to write tests for core functionality in `test_emotion_detector.py`.

### Task 6: Web Deployment Using Flask

Create a web interface using Flask (`app.py`) that allows users to input text and view emotion analysis results.

### Task 7: Incorporate Error Handling

Handle common errors like empty inputs, network/API issues, or invalid responses gracefully with error messages.

### Task 8: Static Code Analysis

Run a tool like `pylint` or `flake8` and aim for clean, well-documented, and readable code.

## Running the Application

```bash
flask run
```

Visit `http://localhost:5000` to access the web interface.


## Testing

Run the test suite using:

```bash
pytest
```

or

```bash
python -m unittest discover
```


## Code Analysis

To perform static code analysis:

```bash
pylint app.py emotion_detector.py
```

or

```bash
flake8 .
```


## Error Handling

The application includes robust error handling for:

- Empty or invalid user input
- API call failures
- Unexpected server errors


## Deployment

This project can be deployed on any platform that supports Flask, such as:

- Render
- Heroku
- AWS Elastic Beanstalk
- Google App Engine

Follow provider-specific instructions for deployment.


## Acknowledgments

- IBM Watson NLP API documentation
- Flask documentation

## License
This project is provided as part of an academic course and is intended for educational purposes.

