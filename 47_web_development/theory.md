# Web Development - Theory

## Table of Contents

1. [HTTP Fundamentals](#http-fundamentals)
2. [REST API Concepts](#rest-api-concepts)
3. [Requests Library](#requests-library)
4. [Flask Framework](#flask-framework)
5. [FastAPI Framework](#fastapi-framework)
6. [Web Patterns](#web-patterns)

---

## HTTP Fundamentals

### What is HTTP?

HTTP (HyperText Transfer Protocol) is a request-response protocol used for transferring data across the web.

```
Client Request          Server Response
    |                       |
    |----- HTTP Request --->|
    |<---- HTTP Response ----|
    |
```

### HTTP Methods

| Method | Purpose | Body | Safe | Idempotent |
|--------|---------|------|------|-----------|
| GET | Retrieve data | No | Yes | Yes |
| POST | Create new resource | Yes | No | No |
| PUT | Replace entire resource | Yes | No | Yes |
| PATCH | Partial update | Yes | No | No |
| DELETE | Remove resource | No | Yes | Yes |
| HEAD | Like GET, no body | No | Yes | Yes |
| OPTIONS | Get allowed methods | No | Yes | Yes |

### HTTP Status Codes

```
1xx: Information
  100 Continue

2xx: Success
  200 OK
  201 Created
  204 No Content

3xx: Redirection
  301 Moved Permanently
  302 Found
  304 Not Modified

4xx: Client Error
  400 Bad Request
  401 Unauthorized
  403 Forbidden
  404 Not Found

5xx: Server Error
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable
```

### HTTP Request Structure

```
GET /api/posts/1 HTTP/1.1
Host: example.com
Content-Type: application/json
User-Agent: Mozilla/5.0
Authorization: Bearer token123

{"filter": "important"}
```

Components:
- **Method & Path**: GET /api/posts/1
- **Protocol**: HTTP/1.1
- **Headers**: Metadata about request
- **Body**: Optional data (JSON, form, etc)

### HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 256
Set-Cookie: sessionid=abc123

{
  "id": 1,
  "title": "Sample Post",
  "body": "Content here"
}
```

Components:
- **Status Line**: HTTP/1.1 200 OK
- **Headers**: Metadata about response
- **Body**: Response data

---

## REST API Concepts

### REST Principles

REST (Representational State Transfer) is an architectural style for web APIs.

**Key Principles:**

1. **Client-Server**: Separation of concerns
2. **Statelessness**: No client context on server
3. **Uniform Interface**: Consistent API design
4. **Resource-Oriented**: URLs represent resources
5. **Representation**: JSON/XML formats
6. **HATEOAS**: Links to related resources (optional)

### Resource-Oriented Design

```
Resources are identified by URLs:

/users              - Collection of users
/users/1            - Specific user
/users/1/posts      - User's posts
/users/1/posts/5    - Specific post by user
```

### Standard CRUD Operations

```
Create  → POST /users
Read    → GET /users/1
Update  → PUT /users/1 (full) or PATCH /users/1 (partial)
Delete  → DELETE /users/1
List    → GET /users
```

### Response Format

Consistent JSON response format:

```json
{
  "status": "success",
  "code": 200,
  "data": {
    "id": 1,
    "name": "John",
    "email": "john@example.com"
  }
}
```

Error response:

```json
{
  "status": "error",
  "code": 400,
  "message": "Invalid email format",
  "errors": {
    "email": ["Invalid email format"]
  }
}
```

### Query Parameters

```
GET /users?page=1&limit=10&sort=name

Query parameters:
- page: 1
- limit: 10
- sort: name

Common uses:
- Pagination: page, limit, offset
- Filtering: status, category, search
- Sorting: sort, order
```

---

## Requests Library

### Basic Requests

```python
import requests

# GET request
response = requests.get('https://example.com/api/posts')
print(response.status_code)      # 200
print(response.text)              # Raw HTML/JSON string
print(response.json())            # Parsed JSON

# POST request
data = {'title': 'New Post', 'body': 'Content'}
response = requests.post('https://example.com/api/posts', json=data)

# PUT request
response = requests.put('https://example.com/api/posts/1', json=data)

# DELETE request
response = requests.delete('https://example.com/api/posts/1')
```

### Request Headers

```python
headers = {
    'User-Agent': 'My App 1.0',
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
```

### Query Parameters

```python
# Method 1: In URL
response = requests.get('https://example.com/api/posts?page=1&limit=10')

# Method 2: params argument (cleaner)
params = {'page': 1, 'limit': 10}
response = requests.get('https://example.com/api/posts', params=params)
```

### Request Body

```python
# JSON body
response = requests.post(url, json={'key': 'value'})

# Form data
response = requests.post(url, data={'username': 'john', 'password': 'secret'})

# File upload
with open('file.txt', 'rb') as f:
    response = requests.post(url, files={'upload': f})
```

### Response Handling

```python
response = requests.get(url)

# Check status
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Not found")

# Or use raise_for_status()
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
```

### Session Management

```python
# Create session for multiple requests
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token123'})

# Requests share cookies, headers, etc
response1 = session.get('https://example.com/profile')
response2 = session.get('https://example.com/posts')
```

---

## Flask Framework

### Basic Flask App

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Flask'})

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
```

### URL Routing

```python
from flask import Flask

app = Flask(__name__)

# Simple route
@app.route('/posts')
def get_posts():
    return {'posts': []}

# Route with parameter
@app.route('/posts/<int:post_id>')
def get_post(post_id):
    return {'post_id': post_id}

# Route with multiple parameters
@app.route('/users/<int:user_id>/posts/<int:post_id>')
def get_user_post(user_id, post_id):
    return {'user_id': user_id, 'post_id': post_id}

# Method specification
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    return {'created': True, **data}, 201
```

### Request Handling

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/posts', methods=['POST'])
def create_post():
    # Get JSON data
    data = request.json

    # Get query parameters
    page = request.args.get('page', 1, type=int)

    # Get form data
    username = request.form.get('username')

    # Get headers
    token = request.headers.get('Authorization')

    return jsonify(data)
```

### Response Handling

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify({'status': 'ok'}), 200

@app.route('/created')
def created():
    return jsonify({'id': 1}), 201

@app.route('/not_found')
def not_found():
    return jsonify({'error': 'Not found'}), 404

@app.route('/error')
def error():
    return jsonify({'error': 'Internal error'}), 500
```

### Error Handling

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({'error': 'Division by zero'}), 400
    return jsonify({'result': a / b})
```

### Middleware and Decorators

```python
from functools import wraps
from flask import Flask, jsonify, request

app = Flask(__name__)

def require_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'error': 'JSON required'}), 400
        return f(*args, **kwargs)
    return decorated_function

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/posts', methods=['POST'])
@require_json
@require_auth
def create_post():
    return jsonify(request.json), 201
```

---

## FastAPI Framework

### Basic FastAPI App

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str
    userId: int

@app.get('/')
def read_root():
    return {'message': 'Welcome to FastAPI'}

@app.get('/posts/{post_id}')
def get_post(post_id: int):
    return {'post_id': post_id}

@app.post('/posts')
def create_post(post: Post):
    return {'id': 1, **post.dict()}
```

Run with:
```bash
uvicorn main:app --reload
```

### Path Parameters

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/posts/{post_id}')
def get_post(post_id: int):
    return {'post_id': post_id}

@app.get('/users/{user_id}/posts/{post_id}')
def get_user_post(user_id: int, post_id: int):
    return {'user_id': user_id, 'post_id': post_id}

# Type validation is automatic
# GET /posts/abc → Error (expects int)
# GET /posts/123 → OK
```

### Query Parameters

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/posts')
def list_posts(
    page: int = 1,
    limit: int = 10,
    sort: str = 'date'
):
    return {
        'page': page,
        'limit': limit,
        'sort': sort
    }

# Usage: GET /posts?page=2&limit=20&sort=title
```

### Request Body

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str
    userId: int

@app.post('/posts')
def create_post(post: Post):
    # post is automatically validated
    # JSON parsing and type checking done automatically
    return {'id': 1, **post.dict()}
```

### Data Validation

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Post(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    body: str = Field(..., min_length=1)
    userId: int = Field(..., gt=0)

@app.post('/posts')
def create_post(post: Post):
    # Validation happens automatically
    # Invalid data returns 422 Unprocessable Entity
    return post
```

### Response Models

```python
from fastapi import FastAPI
from pydantic import BaseModel

class PostResponse(BaseModel):
    id: int
    title: str
    body: str

app = FastAPI()

@app.get('/posts/{post_id}', response_model=PostResponse)
def get_post(post_id: int):
    return {'id': post_id, 'title': 'Sample', 'body': 'Content'}
```

### Error Handling

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/posts/{post_id}')
def get_post(post_id: int):
    if post_id < 1:
        raise HTTPException(status_code=400, detail='Invalid ID')
    if post_id > 1000:
        raise HTTPException(status_code=404, detail='Not found')
    return {'id': post_id}
```

---

## Web Patterns

### Request-Response Cycle

```
Client                          Server
  |                              |
  |--- HTTP Request (GET) ----->|
  |                              |
  |                         Parse request
  |                         Process data
  |                         Generate response
  |                              |
  |<--- HTTP Response (200) -----|
  |                              |
   Parse response
   Use data
```

### Statelessness

Each request must contain all information needed:

```python
# BAD: Relies on state
logged_in_users = set()

@app.post('/login')
def login(username: str, password: str):
    # Check credentials
    logged_in_users.add(username)  # Storing state!
    return {'status': 'ok'}

@app.get('/profile')
def profile():
    # Assumes state from login
    return {'user': list(logged_in_users)[0]}

# GOOD: Stateless with tokens
@app.post('/login')
def login(username: str, password: str):
    # Check credentials
    token = generate_token(username)
    return {'token': token}

@app.get('/profile')
def profile(authorization: str = Header(None)):
    # Token contains all needed info
    username = decode_token(authorization)
    return {'user': username}
```

### API Versioning

```python
from fastapi import FastAPI

app = FastAPI()

# Version in URL path
@app.get('/v1/posts')
def get_posts_v1():
    return {'posts': []}

@app.get('/v2/posts')
def get_posts_v2():
    # Enhanced version
    return {'posts': [], 'total': 0}

# Or version in headers
@app.get('/posts')
def get_posts(api_version: str = Header('v1')):
    if api_version == 'v2':
        return {'posts': [], 'total': 0}
    return {'posts': []}
```

---

## Summary

### HTTP & REST
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes and meanings
- REST principles and resource design
- Request/response structure

### Requests Library
- Making HTTP requests (GET, POST, etc)
- Headers and authentication
- Query parameters and request body
- Response handling and error checking

### Flask
- Route definition and HTTP methods
- Request/response handling
- Error handlers and decorators
- Building simple APIs

### FastAPI
- Modern async framework
- Automatic type validation
- Automatic API documentation
- Request/response models

### Patterns
- Client-server architecture
- Statelessness principle
- API versioning strategies
- Error handling patterns
