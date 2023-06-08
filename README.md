# MongoDB RESTful API
This project is a MongoDB database implemented as a RESTful API. Users can store and retrieve sentences in the database. Each user starts with 6 tokens and storing or retrieving a sentence costs one token.
# Installation
To run the project, you need to have Docker installed on your machine. Once Docker is installed, you can clone the repository and use the provided docker-compose.yml file to build and run the project. Make sure to provide your mongodb url in the app.py file.

## Usage

1. **Build the Docker image:**

    ```shell
    docker-compose build
    ```

2. **Run the Docker container:**

    ```shell
    docker-compose up
    ```

3. **The API is now available at `localhost:5000`.**

## Endpoints

The API includes the following endpoints:

- `POST /register`: Registers a new user.

    Request body: 
    ```json
    { 
        "username": "<username>", 
        "password": "<password>" 
    }
    ```
    Response: 
    ```json
    { 
        "status": 200, 
        "msg": "You successfully signed up for the API" 
    }
    ```

- `POST /store`: Stores a sentence for a user.

    Request body: 
    ```json
    { 
        "username": "<username>", 
        "password": "<password>", 
        "sentence": "<sentence>" 
    }
    ```
    Response: 
    ```json
    { 
        "status": 200, 
        "msg": "Sentence saved successfully" 
    }
    ```

- `POST /get`: Retrieves the stored sentence for a user.

    Request body: 
    ```json
    { 
        "username": "<username>", 
        "password": "<password>" 
    }
    ```
    Response: 
    ```json
    { 
        "status": 200, 
        "sentence": "<sentence>" 
    }
    ```

Remember, each operation (storing or retrieving a sentence) costs one token, and each user starts with 6 tokens.

## Dependencies

This project depends on several Python packages:

- Flask: The web framework for building the API.
- Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs.
- PyMongo: A Python wrapper for MongoDB.
- Certifi: A carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
- Bcrypt: A Python binding for the bcrypt package for password hashing.

These dependencies are listed in the requirements.txt file and will be installed in the Docker container.




