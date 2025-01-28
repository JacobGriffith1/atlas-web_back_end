# Basic Authentication
Project for Atlas School

## Learning Objectives
At the end of this project, understand:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Tasks

## 0. Simple-Basic-API
Download and start your project from this [archive.zip](Basic_authentication\basic_authentication-archive)
In this archive, you will find a simple API with one model: ```User```. Storage of these users is done via a serialization/deserialization in files.
**Setup and Start Server**
```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```
**Use the API (in another tab or in your browser)**
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```

## 1. Error Handler: Unauthorized
What's the HTTP status code for a request unauthorized? ```401```, of course!
Edit ```api/v1/app.py```:
- Add a new error handler for this status code, the response must be:
    - a JSON: ```{"error": "Unauthorized"}```
    - status code ```401```
    - you must use ```jsonify``` from Flask
For testing this new error handler, add a new endpoint in ```api/v1/views/index.py```:
- Route: ```GET /api/v1/unauthorized```
- This endpoint must raise a 401 error by using ```abort``` - [Custom Error Pages](https://flask.palletsprojects.com/en/stable/errorhandling/#custom-error-pages)
By calling ```abort(401)```, the error handler for 401 will be executed.
In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:50:40 GMT
< 
{
  "error": "Unauthorized"
}
* Closing connection 0
bob@dylan:~$
```

## 2. Error Handler: Forbidden
What's the HTTP status code for a request where the user is authenticated but not allowed to access a resource? ```403```, of course!
Edit ```api/v1/app.py```:
- Add a new error handler for this status code, the response must be:
    - a JSON: ```{"error": "Forbidden"}```
    - status code ```403```
    - you must use ```jsonify``` from Flask
For testing this new error handler, add a new endpoint in ```api/v1/views/index.py```:
- Route: ```GET /api/v1/forbidden```
- This endpoint must raise a 403 error by using ```abort``` - [Custom Error Pages](https://flask.palletsprojects.com/en/stable/errorhandling/#custom-error-pages)
By calling ```abort(403)```, the error handler for 403 will be executed.
In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/forbidden HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:54:22 GMT
< 
{
  "error": "Forbidden"
}
* Closing connection 0
bob@dylan:~$
```

## 3. Auth Class
Now you will create a class to manage the API authentication.
- Create a folder ```api/v1/auth```
- Create an empty file ```api/v1/auth/__init__.py```
- Create the class ```Auth```:
    - in the file ```api/v1/auth/auth.py```
    - import ```request``` from ```flask```
    - class name ```Auth```
    - public method ```def require_auth(self, path: str, excluded_paths: List[str]) -> bool:``` that returns ```False``` - ```path``` and ```excluded_paths``` will be used later; now, you don't need to take care of them
    - public method ```def authorization_header(self, request=None) -> str:``` that returns ```None``` - ```request``` will be the Flask request object
    - public method ```def current_user(self, request=None) -> TypeVar('User'):``` that returns ```None``` - ```request``` will be the Flask request object
The class is the template for all authentication system you will implement.

## 4. Define Which Routes Don't Need Authentication
Update the method ```def require_auth(self, path: str, excluded_paths: List[str]) -> bool:``` in ```Auth``` that returns ```True``` if the ```path``` is not in the list of strungs ```excluded_paths```:
- Returns ```True``` if ```path``` is ```None```
- Returns ```True``` if ```excluded_paths``` is ```None``` or empty
- Returns ```False``` if ```path``` is in ```excluded_paths```
- You can assume ```excluded_paths``` contains string path always ending by a ```/```
- This method must be slash tolerant: ```path=/api/v1/status``` and ```path=/api/v1/status/``` must be returned ```False``` if ```excluded_paths``` contains ```/api/v1/status/```

## 5. Request Validation!
Now you will validate all requests to secure the API:
Update the method ```def authorization_header(self, request=None) -> str:``` in ```api/v1/auth/auth.py```:
- If ```request``` is ```None```, returns ```None```
- If ```request``` doesn't contain the header key ```Authorization```, returns ```None```
- Otherwise, return the value of the header request ```Authorization```
Update the file ```api/v1/app.py```:
- Create a variable ```auth``` initialized to ```None``` after the ```CORS``` definition
- Based on the environment variable ```AUTH_TYPE```, load and assign the right instance of authentication to ```auth```
- If ```auth```:
    - Import ```Auth``` from ```api.v1.auth.auth```
    - Create an instance of ```Auth``` and assign it to the variable ```auth```
Now the biggest piece is the filtering of each request. For that, you will use the Flask method [before_request](https://flask.palletsprojects.com/en/stable/api/)
- Add a method in ```api/v1/app.py``` to handler ```before_request```
    - If ```auth``` is ```None```, do nothing
    - If ```request.path``` is not part of this list ```['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']```, do nothing - you must use the method ```require_auth``` from the ```auth``` instance
    - If ```auth.authorization_header(request)``` returns ```None```, raise the error ```401``` - you must use ```abort```
    - If ```auth.current_user(request)``` returns ```None```, raise the error ```403``` - you must use ```abort```
In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
```

## 6. Basic Auth
Create a class ```BasicAuth``` that inherits from ```Auth```. For the moment, this class will be empty.
Update ```api/v1/app.py``` for using ```BasicAuth``` class instead of ```Auth``` depending on the value on the value of the environmental variable ```AUTH_TYPE```. If ```AUTH_TYPE``` is equal to ```basic_auth```:
- Import ```BasicAuth``` from ```api.v1.auth.basic_auth```
- Create an instance of ```BasicAuth``` and assign it to the variable ```auth```
Otherwise, keep the previous mechanism with ```aut``` an instance of ```Auth```.
In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
```
