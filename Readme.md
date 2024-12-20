User Management API
===================

This project provides a set of APIs for user registration, login, linking IDs, and managing user-related data, built with FastAPI and MongoDB.

Features
--------

*   **User Registration**: Allows users to register with a username, email, and password.
*   **User Login**: Allows registered users to log in with their email and password.
*   **Link IDs**: Allows users to link an external ID to their profile.
*   **View User Data**: Provides a route to fetch user data, including the `joined_date`.
*   **Delete User**: Allows the deletion of a user and their associated linked IDs.

Requirements
------------

*   Python 3.10 or higher
*   MongoDB (installed locally or remotely)
*   Required dependencies are listed in the `requirements.txt`

Installation
------------

1.  Clone the repository:
    ```
    git clone https://github.com/kunalarya873/remotebricks.git

    cd remotebricks/
    ```
2.  Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate  
    
    # On Windows, use venv\Scripts\activate

    ```
    
3.  Install the required dependencies:
    
    `pip install -r requirements.txt` 
    
4.  Ensure that MongoDB is running locally or modify the MongoDB connection string in `main.py` to connect to your MongoDB instance.
    

Project Structure
-----------------

*   `src/app/routers/`: Contains the API route definitions for users, linking IDs, and joining data.
*   `src/app/models/`: Defines Pydantic models for user registration, login, and linked IDs.
*   `src/app/utils/`: Contains utility functions like password hashing and user retrieval by email.
*   `src/app/db.py`: Handles database connections and operations.

Running the Application
-----------------------

To start the FastAPI application:

`uvicorn src.app.main:app --reload` 

The API will be available at `http://localhost:8000`.

API Endpoints
-------------

### 1\. Register a New User

**POST** `/user/register/`

Request body:

```
{
  "username": "user1",
  "email": "user1@example.com",
  "password": "password123"
}
``` 

### 2\. Login a User

**POST** `/user/login/`

Request body:
```
{
  "email": "user1@example.com",
  "password": "password123"
}
``` 

### 3\. Link an ID to a User

**POST** `/link/link-id/`

Request body:

```
{
  "email": "user1@example.com",
  "linked_id": "external-id-123"
}
``` 

### 4\. Get User Data by Email

**GET** `/join/joined-data/{email}/`

Returns the user data along with the linked IDs.

### 5\. Delete User by Email

**DELETE** `/join/delete-user/{email}/`

### 6\. Custom Swagger Documentation

**GET** `/docs/`

This endpoint provides custom Swagger UI documentation for the API.

Database Configuration
----------------------

The app connects to a MongoDB instance located at `mongodb://localhost:27017`. You can modify the connection string in `src/app/main.py` if you're using a different MongoDB setup.

Testing
-------

To test the APIs, you can use any API testing tool like Postman or curl. The server will automatically reload on code changes if you run it in development mode with the `--reload` option.

Logs
----

The application uses Python's built-in `logging` library to log user data and other important information. You can configure the logging level and format in the application as needed.

Security
--------

*   Passwords are hashed using `bcrypt` to ensure security.
*   The `joined_date` field is automatically generated when a user registers.