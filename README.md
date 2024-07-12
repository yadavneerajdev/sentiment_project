# Sentiment Analysis Application

This repository contains a sentiment analysis application with a front-end built using React and a back-end server using Flask. The application predicts the sentiment (positive or negative) of a given text input.

## Table of Contents
- [Getting Started](#getting-started)
- [Front-End Setup](#front-end-setup)
- [Back-End Setup](#back-end-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

### Front-End Setup

1. Navigate to the front-end directory:
    ```bash
    cd path/to/frontend-directory
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Start the front-end development server:
    ```bash
    npm run start
    ```

The React application should now be running on `http://localhost:3000`.

### Back-End Setup

1. Navigate to the Flask server directory:
    ```bash
    cd path/to/flask-server-directory
    ```

2. Install the required dependencies:
    ```bash
    pip install Flask
    pip install Flask-CORS
    pip install numpy
    pip install tensorflow
    ```

3. Start the Flask server:
    ```bash
    python server.py
    ```

The Flask server should now be running on `http://127.0.0.1:5000`.

## Usage

Once both the front-end and back-end servers are running, you can use the application to input text and receive sentiment predictions.

1. Open your browser and navigate to `http://localhost:3000`.
2. Enter the text you want to analyze in the input field.
3. Submit the text to receive the sentiment prediction.

## API Endpoints

### `GET /members`

Returns a list of members.

**Response:**
```json
{
  "members": ["Member1", "Member2", "Member3"]
}
