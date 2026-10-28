# Flask API Assignment

## Description
This project is a basic Flask application that returns JSON responses. It includes a GET endpoint for a greeting and a POST endpoint that calculates the sum of a list of numbers.

## Setup

Create and activate a virtual environment:

python3 -m venv venv

source venv/bin/activate

Install the required dependencies:

pip install Flask pytest

## Run the Application

Run the Flask server with:

python app.py

The application will run locally on port 5000:

http://127.0.0.1:5000

## Endpoints

### GET /hello

Returns a JSON greeting. An optional name can be provided.

Example:

http://127.0.0.1:5000/hello?name=Matiwos

Example response:

{"message":"Hello, Matiwos!"}

### POST /sum

Accepts a JSON list of numbers and returns their sum.

Example request:

{"numbers":[1,2,3]}

Example response:

{"sum":6}

Invalid requests return a 400 status code.

## Testing

Run the automated tests with:

pytest test_app.py

Test result:

4 passed

The tests verify the hello route, default greeting, sum route, and error handling.