# User Authentication Service
Project for Atlas School

## Learning Objectives
At the end of this project, understand:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes
<br />

## Tasks

## 0. User Model
In this task you will create a SQLAlchemy model name ```User``` for a database table name ```users``` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).
The model will have the following attributes:
- ```id```, the integer primary key
- ```email```, a non-nullable string
- ```hashed_password```, a non-nullable string
- ```session_id```, a nullable string
- ```reset_token```, a nullable string
<br />

## 1. Create User
In this task, you will complete the ```DB``` class provided below to implement the ```add_user``` method.
```
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```
Note that ```DB._session is a private property and hence should NEVER be used from outside the ```DB``` class.
Implement the ```add_user``` method, which has two required string arguments: ```email``` and ```hashed_password```, and returns a ```User``` object. The method should save the user to the database. No validations are required at this stage.
<br />

## 2. Find User
In this task you will implement the ```DB.find_user_by``` method. This method takes in arbitrary keyword arguments and returns the first row found in the ```users``` table as filtered by the method's input arguments. No validation of input arguments required at this point/
Make sure that SQLAlchemy's ```NoResultFound``` and ```InvalidRequestError``` are raised when no results are found, or when wrong query arguments are passed, respectively.
**Warning:**
- ```NoResultFound``` has been moved from ```sqlalchemy.orm.exc``` to ```sqlalchemy.exc``` between the version 1.3.x and 1.4.x of SQLAlchemy - please make sure you are importing it from ```sqlalchemy.orm.exc```
<br />

## 3. Update User
In this task, you will imlement the ```DB.update_user``` method that takes as argument a required ```user_id``` integer and arbitrary keyword arguments, and returns ```None```.
The method will use ```find_user_by``` to locate the user to update, then will upate the user's attributes as passed in the method's arguments then commit changes to the database.
If an argument that does not correspond to a user attribute is passed, raise a ```ValueError```.
<br />

## 4. Hash Password
In this task, you will define a ```_hash_password``` method that takes in a ```password``` string arguments and returns bytes.
The returned bytes are a salted hash of the input password, hashed with ```bcrypt.hashpw```.
<br />

## 5. Register User
In this task, you will implement the ```Auth.register_user``` in the ```Auth``` class provided below:
```
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
```
Note that ```Auth._db``` is a private property and should NEVER be used from outside the class.
```Auth.register_user``` should take mandatory ```email``` and ```password``` string arguments and return a ```User``` object.
If a user already exists with the passed email, raise a ```ValueError``` with the message ```User <user's email> already exists```.
If not, hash the password with ```_hash_password```, save the user to the database using ```self._db``` and return the ```User``` object.
<br />

## 6. Basic Flask App
In this task, you will set up a basic Flask app.
Create a Flask app that has a single ```GET``` route (```"/"```) and use ```flask.jsonify``` to return a JSON payload of the form:
```
{"message": "Bienvenue"}
```
Add the following code at the end of the module:
```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```
<br />

## 7. Register User
In this task, you will implement the end-point to register a user. Define a ```users``` function that implements the ```POST /users``` route.
Import the ```Auth``` object and instantiate it at the root of the module as such:
```
from auth import Auth


AUTH = Auth()
```
The end-point should expect two form data fields: ```"email"``` and ```"password"```. If the user does not exist, the end-point should register it and respond with the following JSON payload:
```
{"email": "<registered email>", "message": "user created"}
```
If the user is already registered, catch the exception and return a JSON payload of the form
```
{"message": "email already registered"}
```
and return a 400 status code
Remember that you should only use ```AUTH``` in this app. ```DB``` is a lower abstraction that is proxied by ```Auth```.
*Terminal 1:*
```
bob@dylan:~$ python3 app.py 
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
*Terminal 2:*
```
bob@dylan:~$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 40
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 52
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:03:18 GMT
< 
{"email":"bob@me.com","message":"user created"}

bob@dylan:~$
bob@dylan:~$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 40
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 400 BAD REQUEST
< Content-Type: application/json
< Content-Length: 39
< Server: Werkzeug/1.0.1 Python/3.7.3
< Date: Wed, 19 Aug 2020 00:03:33 GMT
< 
{"message":"email already registered"}
bob@dylan:~$
```
<br />

## 8. Credentials Validation
In this task, you will implement the ```Auth.valid_login``` method. It should expect ```email``` and ```password``` required arguments and return a boolean.
Try locating the user by email. If it exists, check the password with ```bcrypt.checkpw```. If it matches, return ```True```. In any other case, return ```False```.
<br />

## 9. Generate UUIDs
In this task you will implement a ```_generate_uuid``` function in the ```auth``` module. The function should return a string representaion of a new UUID. Use the ```uuid``` module.
Note that the method is private to the ```auth``` module and should **NOT** be used outside of it.
<br />

## 10. Get Session ID
In this task, you will implement the ```Auth.create_session``` method. It takes an ```email``` string argument and returns the session ID as a string.
The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user's ```session_id```, then return the session ID.
Remember that only public methods of ```self._db``` can be used.
<br />

## 11. Log In
In this task, you will implement a ```login``` function to respond to the ```POST /sessions``` route.
The request is expected to contain form data with ```"email"``` and a ```"password"``` fields.
If the login information is incorrect, use ```flask.abort``` to respond with a 401 HTTP status.
Otherwise, create a new session for the user, store the session ID as a cookie with key ```"session_id"``` on the response and return a JSON payload of the form
```
{"email": "<user email>", "message": "logged in"}
```
<br />

## 12. Find User by Session ID
In this task, you will implement the ```Auth.get_user_from_session_id``` method. It takes a single ```session_id``` string argument and returns the corresponding ```User``` or ```None```.
If the session ID is ```None``` or no user is found, return ```None```. Otherwise, return the corresponding user.
Remember to only use public methods of ```self._db```.
<br />

## 13. Destroy Session
In this task, you will implement ```Auth.destroy_session```. The method takes a single ```user_id``` integer argument and returns ```None```.
The method updates the corresponding user's session ID to ```None```.
Remember to only use public methods of self._db.
<br />

## 14. Log Out
In this task, you will implement a ```logout``` function to respond to the ```DELETE /sessions``` route.
The request is expected to contain the session ID as a cookie with key ```"session_id"```.
Find the user with the requested session ID. If the user exists, destroy the session and redirect the user to ```GET /```. If the user does not exist, respond with a 403 HTTP status.
<br />

## 15. User Profile
In this task, you will implement a ```profile``` function to respond to the ```GET /profile``` route.
The request is expected to contain a ```session_id``` cookie. Use it to find the user. If the user exists, respond with a 200 HTTP status and the following JSON payload:
```
{"email": "<user email>"}
```
If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.
<br />

## 16. Generate Reset Password Token
In this task, you will implement the ```Auth.get_reset_password_token``` method. It takes an ```email``` string argument and returns a string.
Find the user corresponding to the email. If the user does not exist, raise a ```ValueError``` exception. If it exists, generate a UUID and update the user's ```reset_token``` database field. Return the token.
<br />

## 17. Get Reset Password Token
In this task, you will implement a ```get_reset_password_token``` function to respond to the ```POST /reset_password``` route.
The request is expected to contain form data with the ```"email"``` field.
If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:
```
{"email": "<user email>", "reset_token": "<reset token>"}
```
<br />

## 18. Update Password
In this task, you will implement the ```Auth.update_password``` method. It takes ```reset_token``` string argument and a ```password``` string argument and returns ```None```.
Use the ```reset_token``` to find the corresponding user. If it doesn't exist, raises a ```ValueError``` exception.
Otherwise, hash the password and update the user's ```hashed_password``` field with the new hashed password and the ```reset_token``` field to ```None```.
<br />

## 19. Update Password End-Point
In this task, you will implement the ```update_password``` function in the ```app``` module to respond to the ```PUT /reset_password``` route.
The request is expected to contain form data with fields ```"email"```, ```"reset_token"``` and ```"new_password"```.
Update the password. If the token is invalid, catch the exception with a 403 HTTP code.
If the token is valid, respond with a 200 HTTP code and the following JSON payload:
```
{"email": "<user email>", "message": "Password updated"}
```
<br />
