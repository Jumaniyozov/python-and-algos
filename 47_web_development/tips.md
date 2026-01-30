# Web Development - Tips and Best Practices

## Requests Library Tips

### 1. Always Handle Errors

```python
# GOOD: Comprehensive error handling
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code}")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# BAD: No error handling
response = requests.get(url)
data = response.json()  # May crash!
```

### 2. Use Sessions for Multiple Requests

```python
# GOOD: Reuse session
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token'})

for url in urls:
    response = session.get(url)
    # Headers automatically included

# BAD: Repeat headers for each request
for url in urls:
    headers = {'Authorization': 'Bearer token'}
    response = requests.get(url, headers=headers)
```

### 3. Set Timeouts

```python
# GOOD: Always set timeout
response = requests.get(url, timeout=10)

# BAD: Can hang indefinitely
response = requests.get(url)

# Different timeouts for connect and read
response = requests.get(url, timeout=(5, 10))
```

### 4. Validate Response Before Using

```python
# GOOD: Check before processing
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")

# Or use raise_for_status()
response = requests.get(url)
try:
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError:
    print("Bad status code")
```

---

## Flask Tips

### 1. Proper Request/Response Pattern

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# GOOD: Proper structure
@app.route('/api/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'GET':
        return jsonify({'items': []})
    elif request.method == 'POST':
        data = request.json
        if not data:
            return jsonify({'error': 'JSON required'}), 400
        return jsonify(data), 201

# Or separate methods
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': []})

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    if not data:
        return jsonify({'error': 'JSON required'}), 400
    return jsonify(data), 201
```

### 2. Use jsonify for All Responses

```python
# GOOD: Always jsonify
@app.route('/data')
def get_data():
    return jsonify({'key': 'value'})

# BAD: Inconsistent response types
@app.route('/data')
def get_data():
    return {'key': 'value'}  # Dict, not JSON string
```

### 3. Consistent Error Response Format

```python
# GOOD: Consistent error format
def error_response(message, status_code):
    return jsonify({
        'error': True,
        'message': message,
        'status_code': status_code
    }), status_code

@app.route('/items/<int:item_id>')
def get_item(item_id):
    if not item:
        return error_response('Item not found', 404)
    return jsonify(item)
```

### 4. Use Blueprints for Organization

```python
from flask import Flask, Blueprint

app = Flask(__name__)

# Create blueprints for different modules
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/items')
def get_items():
    return {'items': []}

@api_bp.route('/users')
def get_users():
    return {'users': []}

# Register blueprint
app.register_blueprint(api_bp)
```

### 5. Proper Status Codes

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/items', methods=['POST'])
def create_item():
    # 201 Created for successful creation
    return jsonify({'id': 1}), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # 204 No Content for successful deletion
    return '', 204

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # 404 for not found
    return jsonify({'error': 'Not found'}), 404

@app.route('/invalid')
def invalid():
    # 400 for bad request
    return jsonify({'error': 'Bad request'}), 400
```

---

## FastAPI Tips

### 1. Use Pydantic Models for Validation

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# GOOD: Use models with validation
class Item(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(1, ge=0)

@app.post('/items')
def create_item(item: Item):
    # Data is automatically validated
    return item

# BAD: No validation
@app.post('/items')
def create_item_bad(item: dict):
    # No automatic validation
    return item
```

### 2. Use Type Hints Throughout

```python
from fastapi import FastAPI, Path, Query
from typing import Optional, List

app = FastAPI()

# GOOD: Clear types
@app.get('/items/{item_id}')
def get_item(
    item_id: int = Path(..., gt=0),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
) -> dict:
    return {'item_id': item_id, 'skip': skip, 'limit': limit}

# BAD: No types
@app.get('/items/{item_id}')
def get_item_bad(item_id, skip=0, limit=10):
    return {'item_id': item_id}
```

### 3. Proper Error Handling with HTTPException

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# GOOD: Use HTTPException
@app.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail='Invalid ID')
    if item_id > 1000:
        raise HTTPException(status_code=404, detail='Not found')
    return {'id': item_id}

# BAD: Returning tuple instead of raising exception
@app.get('/items/{item_id}')
def get_item_bad(item_id: int):
    if item_id > 1000:
        return {'error': 'Not found'}, 404  # Wrong!
    return {'id': item_id}
```

### 4. Response Models for Output

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemDB(BaseModel):
    id: int
    title: str
    secret_field: str  # We don't want to return this

class ItemResponse(BaseModel):
    id: int
    title: str

@app.get('/items/{item_id}', response_model=ItemResponse)
def get_item(item_id: int):
    # Only fields in ItemResponse are returned
    return {
        'id': item_id,
        'title': 'Item',
        'secret_field': 'hidden'  # Not returned!
    }
```

### 5. Documentation with Docstrings

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
def get_item(item_id: int):
    """
    Get a specific item by ID.

    Args:
        item_id: The ID of the item to retrieve (1-1000)

    Returns:
        Dictionary containing item details
    """
    return {'id': item_id}

# Documentation automatically shown at /docs
```

---

## REST API Best Practices

### 1. Resource-Oriented URLs

```python
# GOOD: Resource-oriented
GET    /api/users           # List all users
GET    /api/users/123       # Get user 123
POST   /api/users           # Create user
PUT    /api/users/123       # Update user 123
DELETE /api/users/123       # Delete user 123

# BAD: Action-oriented
GET    /api/getUser?id=123
POST   /api/createUser
PUT    /api/updateUser?id=123
DELETE /api/deleteUser?id=123
```

### 2. Consistent Response Format

```python
# GOOD: Consistent format
{
  "status": "success",
  "code": 200,
  "data": {
    "id": 1,
    "name": "Item"
  }
}

# Error:
{
  "status": "error",
  "code": 400,
  "message": "Invalid data",
  "errors": {"field": ["Error message"]}
}

# BAD: Inconsistent
Success: {"id": 1, "name": "Item"}
Error: {"error": "Something failed"}
```

### 3. Pagination for List Endpoints

```python
# GOOD: Include pagination info
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150,
    "total_pages": 8
  }
}

# Usage: GET /api/items?page=1&per_page=20
```

### 4. Versioning Strategy

```python
# Option 1: URL path
GET /api/v1/items
GET /api/v2/items

# Option 2: Header
curl -H "API-Version: 2" http://api.example.com/items

# Option 3: Accept header
curl -H "Accept: application/vnd.api+json;version=2" http://api.example.com/items
```

### 5. Documentation

```python
# GOOD: API documentation
"""
API Documentation

Base URL: https://api.example.com/v1

Endpoints:

GET /items
  - List all items
  - Query params: page (1+), limit (1-100)
  - Returns: {items: [...], total: int}

GET /items/{id}
  - Get specific item
  - Returns: Item object or 404

POST /items
  - Create new item
  - Body: {name: string, price: float}
  - Returns: Created Item or 400 on validation error

PUT /items/{id}
  - Update item
  - Body: {name?: string, price?: float}
  - Returns: Updated Item or 404

DELETE /items/{id}
  - Delete item
  - Returns: 204 No Content
"""
```

---

## Debugging Tips

### 1. Use Print Statements

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/items', methods=['POST'])
def create_item():
    print("Headers:", dict(request.headers))
    print("Raw data:", request.data)
    print("JSON data:", request.json)

    data = request.json
    return jsonify(data), 201
```

### 2. Use curl for Testing

```bash
# Simple GET
curl http://localhost:5000/items

# GET with headers
curl -H "Authorization: Bearer token" http://localhost:5000/items

# POST with JSON
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Item"}'

# Verbose output
curl -v http://localhost:5000/items

# Show headers
curl -i http://localhost:5000/items
```

### 3. Use Postman or Insomnia

- GUI for testing APIs
- Save requests for reuse
- Organize requests in collections
- Export for team sharing

### 4. Enable Debug Mode

```python
# Flask debug mode
if __name__ == '__main__':
    app.run(debug=True)

# FastAPI debug with uvicorn
# uvicorn main:app --reload
```

---

## Performance Tips

### 1. Cache Responses

```python
from flask import Flask
from functools import lru_cache
import time

app = Flask(__name__)

@lru_cache(maxsize=128)
def get_expensive_data(key):
    time.sleep(2)  # Simulate slow operation
    return {'key': key, 'value': 'data'}

@app.route('/data/<key>')
def get_data(key):
    return get_expensive_data(key)
```

### 2. Limit Request Size

```python
from flask import Flask

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
```

### 3. Use Async for I/O

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get('/items')
async def list_items():
    # Async operations (database, API calls, etc)
    await asyncio.sleep(0.1)
    return {'items': []}
```

### 4. Batch Operations

```python
# GOOD: Single request with multiple items
POST /api/items/batch
{
  "items": [
    {"name": "Item 1"},
    {"name": "Item 2"},
    {"name": "Item 3"}
  ]
}

# BAD: Multiple requests
POST /api/items {"name": "Item 1"}
POST /api/items {"name": "Item 2"}
POST /api/items {"name": "Item 3"}
```

---

## Security Tips

### 1. Validate All Input

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not validate_email(data.get('email', '')):
        return jsonify({'error': 'Invalid email'}), 400
    return jsonify(data), 201
```

### 2. Use HTTPS in Production

```python
# Development
app.run(debug=True)

# Production (use HTTPS)
# Deploy with proper SSL certificates
```

### 3. Sanitize Output

```python
from flask import escape

@app.route('/user/<name>')
def greet(name):
    # Escape HTML characters
    safe_name = escape(name)
    return f'Hello, {safe_name}!'
```

### 4. Rate Limiting

```python
from flask_limiter import Limiter

limiter = Limiter(app)

@app.route('/api/data')
@limiter.limit('10 per minute')
def get_data():
    return {'data': []}
```

---

## Testing

### 1. Test with pytest

```python
# test_api.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get('/api/items')
    assert response.status_code == 200

def test_create_item(client):
    response = client.post('/api/items',
        json={'name': 'Item', 'price': 10})
    assert response.status_code == 201
```

### 2. Test FastAPI with TestClient

```python
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_items():
    response = client.get('/items')
    assert response.status_code == 200

def test_create_item():
    response = client.post('/items',
        json={'title': 'Item', 'price': 10})
    assert response.status_code == 201
```

---

## Checklist Before Deployment

- [ ] All endpoints tested
- [ ] Error handling implemented
- [ ] Input validation in place
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Logging implemented
- [ ] Documentation complete
- [ ] Security headers set
- [ ] CORS configured properly
- [ ] Database migrations run
- [ ] Environment variables set
- [ ] Tests passing
