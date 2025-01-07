# Marriage Matchmaking App

## Brief Description
The Marriage Matchmaking App is a backend application designed to help users find potential matches based on their profile information. The app allows users to create, read, update, and delete profiles with details such as name, age, gender, email, city, and interests.

## What is Provided?
This project provides a basic skeleton for a FastAPI-based backend application. 

#### GitHub Repository: [UrbanMatch-PythonTask](https://github.com/abhishek-UM/UrbanMatch-PythonTask/tree/master)

### Basic Project Structure:

- **main.py**: The main application file with basic CRUD operations for user profiles.
- **models.py**: SQLAlchemy models defining the User schema.
- **database.py**: Database configuration and setup.
- **schemas.py**: Pydantic schemas for data validation and serialization.

### Functionality:

- **Create User Endpoint**: Create a new user profile.
- **Read Users Endpoint**: Retrieve a list of user profiles.
- **Read User by ID Endpoint**: Retrieve a user profile by ID.
- **SQLite Database**: The application uses SQLite as the database to store user profiles.

## What is Required?
### Tasks:
1. **Add User Update Endpoint**:
   - Implement an endpoint to update user details by ID in the `main.py` file.
2. **Add User Deletion Endpoint**:
   - Implement an endpoint to delete a user profile by ID.
3. **Find Matches for a User**:
   - Implement an endpoint to find potential matches for a user based on their profile information.
4. **Add Email Validation**:
   - Add validation to ensure the email field in user profiles contains valid email addresses.

## Instructions:
### Implement the Required Features:
1. Add the necessary code for:
   - **Update User Endpoint**: Update user details by ID.
   - **Delete User Endpoint**: Delete a user profile by ID.
   - **Find Matches Endpoint**: Find potential matches based on user profiles.
   - **Email Validation**: Ensure the email field contains valid email addresses.

2. Test Your Implementation:
   - Verify that users can be updated and deleted correctly.
   - Check that matches are correctly retrieved for a given user.
   - Ensure email validation works as expected.

3. Submit Your Work:
   - Provide the updated code files (`main.py`, `models.py`, `database.py`, and `schemas.py`).
   - Include a brief report explaining your approach and any assumptions made.

## Prerequisites
- **Python 3.7+**: Ensure you have Python 3.7 or higher installed.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **SQLite**: A C library that provides a lightweight disk-based database.

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/abhishek-UM/UrbanMatch-PythonTask.git

2. Navigate to the project directory:
   ```bash
   cd UrbanMatch-PythonTask

3. Install the required dependencies:
  ```bash
   pip install -r requirements.txt

 4. Start the application:
    ```bash
    uvicorn main:app --reload

  5. Access the application in your browser at http://127.0.0.1:8000


## EndPoints:
 1. Create User: POST /users/
 2. Read Users: GET /users/
 3. Read User by ID: GET /users/{user_id}
 4. Update User: PUT /users/{user_id}
 5. Delete User: DELETE /users/{user_id}
 6. Find Matches: GET /users/{user_id}/matches




