# Web Development - Solutions

## Complete Solutions with Explanations

### Requests Library Solutions

#### Solution 1: GET Request Basics

```python
import requests

# Fetch single post
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
post = response.json()
print(f"Post 1 title: {post['title']}")

# Fetch posts for user 2
response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=2')
posts = response.json()
print(f"Retrieved {len(posts)} posts for userId 2")

# First post body
if posts:
    print(f"First post body: {posts[0]['body']}")
```

**Output:**
```
Post 1 title: sunt aut facere repellat provident occaecati...
Retrieved 10 posts for userId 2
First post body: qui architecto voluptatum nesciunt...
```

#### Solution 2: POST and PUT Requests

```python
import requests

# Create new post
new_post = {
    'title': 'My New Post',
    'body': 'This is the content of my new post.',
    'userId': 1
}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=new_post
)
print(f"Create status: {response.status_code}")
print(f"Created post: {response.json()}")

# Update post 1
update_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'Updated body content',
    'userId': 1
}
response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=update_data
)
print(f"\nUpdate status: {response.status_code}")
print(f"Updated post: {response.json()}")
```

**Output:**
```
Create status: 201
Created post: {'userId': 1, 'id': 101, 'title': 'My New Post', ...}

Update status: 200
Updated post: {'id': 1, 'title': 'Updated Title', ...}
```

#### Solution 3: Query Parameters and Filtering

```python
import requests

# Pagination: skip first 5, get next 5
params = {'_start': 5, '_limit': 5}
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params=params
)
posts = response.json()
print(f"Posts 5-10: {len(posts)} posts retrieved")

# Filter by userId
params = {'userId': 2}
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params=params
)
posts = response.json()
print(f"Posts by user 2: {len(posts)} posts")

# Multiple filters
params = {'userId': 1, '_start': 0, '_limit': 3}
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params=params
)
posts = response.json()
print(f"User 1, first 3 posts: {len(posts)} posts")
```

#### Solution 4: Error Handling

```python
import requests

endpoints = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/99999',
    'https://invalid-url-xyz.com/api',
    'https://jsonplaceholder.typicode.com/posts/2'
]

for url in endpoints:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(f"✓ {url[:50]}... : {response.status_code}")
    except requests.exceptions.HTTPError as e:
        print(f"✗ {url[:50]}... : HTTP {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"✗ {url[:50]}... : Connection error")
    except requests.exceptions.Timeout:
        print(f"✗ {url[:50]}... : Timeout")
    except Exception as e:
        print(f"✗ {url[:50]}... : {type(e).__name__}")
```

#### Solution 5: Session Management

```python
import requests
import json

# Create session with headers
session = requests.Session()
session.headers.update({
    'Authorization': 'Bearer demo-token-123',
    'User-Agent': 'MyApp/1.0'
})

# Make multiple requests with same headers
endpoints = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/users/1'
]

for url in endpoints:
    try:
        response = session.get(url)
        print(f"GET {url.split('/')[-2]}/{url.split('/')[-1]}: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Close session
session.close()
```

---

### Flask Solutions

#### Solution 6: Simple Flask API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
items = [
    {'id': 1, 'name': 'Item A', 'price': 29.99},
    {'id': 2, 'name': 'Item B', 'price': 49.99}
]

@app.route('/items', methods=['GET'])
def get_items():
    """Get all items"""
    return jsonify({'items': items})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get specific item by ID"""
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    """Create new item"""
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name field'}), 400

    new_item = {
        'id': max(i['id'] for i in items) + 1,
        'name': data['name'],
        'price': data.get('price', 0)
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**Test:**
```bash
curl http://localhost:5000/items
curl http://localhost:5000/items/1
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"New Item","price":19.99}'
```

#### Solution 7: Query Parameters in Flask

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 999.99},
    {'id': 2, 'name': 'Mouse', 'category': 'electronics', 'price': 25.99},
    {'id': 3, 'name': 'Book', 'category': 'books', 'price': 15.99},
    {'id': 4, 'name': 'Monitor', 'category': 'electronics', 'price': 299.99},
    {'id': 5, 'name': 'Pen', 'category': 'stationery', 'price': 5.99},
]

@app.route('/products', methods=['GET'])
def list_products():
    """List products with optional filtering and sorting"""
    result = products

    # Filter by category
    category = request.args.get('category')
    if category:
        result = [p for p in result if p['category'] == category]

    # Filter by price range
    min_price = request.args.get('minPrice', type=float)
    max_price = request.args.get('maxPrice', type=float)
    if min_price:
        result = [p for p in result if p['price'] >= min_price]
    if max_price:
        result = [p for p in result if p['price'] <= max_price]

    # Sort
    sort_by = request.args.get('sortBy', 'id')
    order = request.args.get('order', 'asc') == 'asc'
    if sort_by in ['id', 'price', 'name']:
        result.sort(key=lambda x: x[sort_by], reverse=not order)

    return jsonify({'products': result, 'count': len(result)})

if __name__ == '__main__':
    app.run(debug=True)
```

**Test:**
```bash
curl "http://localhost:5000/products"
curl "http://localhost:5000/products?category=electronics"
curl "http://localhost:5000/products?minPrice=100&maxPrice=500"
curl "http://localhost:5000/products?category=electronics&sortBy=price&order=desc"
```

#### Solution 8: Request Body Validation

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

users = []

def validate_email(email):
    """Check if email format is valid"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/users', methods=['POST'])
def create_user():
    """Create new user with validation"""
    data = request.json

    # Check if data exists
    if not data:
        return jsonify({'error': 'Request body required'}), 400

    # Validate all fields present
    required_fields = ['name', 'email', 'age']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400

    # Validate name
    name = data['name']
    if not name or not isinstance(name, str):
        return jsonify({'error': 'Name must be non-empty string'}), 400

    # Validate email
    email = data['email']
    if not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    # Validate age
    try:
        age = int(data['age'])
        if age <= 0 or age > 150:
            return jsonify({'error': 'Age must be between 1 and 150'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Age must be a positive integer'}), 400

    # Create user
    new_user = {
        'id': len(users) + 1,
        'name': name,
        'email': email,
        'age': age
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### Solution 9: Error Handling Decorators

```python
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def require_json(f):
    """Decorator: require JSON content type"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        return f(*args, **kwargs)
    return decorated

def require_auth(f):
    """Decorator: require Authorization header"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({'error': 'Authorization header required'}), 401
        if not auth.startswith('Bearer '):
            return jsonify({'error': 'Invalid token format'}), 401
        return f(*args, **kwargs)
    return decorated

def handle_errors(f):
    """Decorator: catch exceptions and return error response"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Internal server error'}), 500
    return decorated

@app.route('/public', methods=['GET'])
def public_endpoint():
    return jsonify({'message': 'Public data'})

@app.route('/protected', methods=['GET'])
@require_auth
def protected_endpoint():
    return jsonify({'message': 'Protected data'})

@app.route('/api/data', methods=['POST'])
@require_json
@require_auth
def create_data():
    data = request.json
    return jsonify({'created': True, 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### Solution 10: Complete CRUD API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
resources = [
    {'id': 1, 'title': 'Item 1', 'description': 'First item'},
    {'id': 2, 'title': 'Item 2', 'description': 'Second item'}
]

# CREATE
@app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Title required'}), 400

    new_resource = {
        'id': max(r['id'] for r in resources) + 1,
        'title': data['title'],
        'description': data.get('description', '')
    }
    resources.append(new_resource)
    return jsonify(new_resource), 201

# READ (list with pagination)
@app.route('/api/resources', methods=['GET'])
def list_resources():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        'resources': resources[start:end],
        'total': len(resources),
        'page': page
    })

# READ (single)
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404
    return jsonify(resource)

# UPDATE
@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404

    data = request.json
    if not data:
        return jsonify({'error': 'Request body required'}), 400

    resource['title'] = data.get('title', resource['title'])
    resource['description'] = data.get('description', resource['description'])
    return jsonify(resource)

# DELETE
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    global resources
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404

    resources = [r for r in resources if r['id'] != resource_id]
    return jsonify({'message': 'Resource deleted'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

---

### FastAPI Solutions

#### Solution 11-15: FastAPI Applications

**Basic Application:**

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    title: str
    description: Optional[str] = None
    price: float

class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float

items = [
    {'id': 1, 'title': 'Item 1', 'description': 'First', 'price': 29.99},
]

@app.get('/')
def read_root():
    return {'message': 'Welcome'}

@app.get('/items', response_model=List[ItemResponse])
def list_items(skip: int = 0, limit: int = 10):
    return items[skip:skip+limit]

@app.get('/items/{item_id}', response_model=ItemResponse)
def get_item(item_id: int):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item

@app.post('/items', response_model=ItemResponse)
def create_item(item: Item):
    new_item = {
        'id': len(items) + 1,
        **item.dict()
    }
    items.append(new_item)
    return new_item

@app.put('/items/{item_id}', response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    existing = next((i for i in items if i['id'] == item_id), None)
    if not existing:
        raise HTTPException(status_code=404, detail='Item not found')

    existing.update(item.dict())
    return existing

@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    global items
    if not any(i['id'] == item_id for i in items):
        raise HTTPException(status_code=404, detail='Item not found')
    items = [i for i in items if i['id'] != item_id]
    return {'message': 'Item deleted'}
```

Run with:
```bash
uvicorn filename:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

---

## Key Patterns

### Error Handling Pattern

```python
try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP {e.response.status_code}: {e.response.reason}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### Validation Pattern

```python
def validate_user(data):
    errors = {}

    if not data.get('name'):
        errors['name'] = 'Name required'

    if not validate_email(data.get('email', '')):
        errors['email'] = 'Invalid email'

    if errors:
        raise ValueError(f"Validation failed: {errors}")

    return True
```

### CRUD Pattern

```
POST   /resource        → Create
GET    /resource        → List
GET    /resource/{id}   → Read
PUT    /resource/{id}   → Update
DELETE /resource/{id}   → Delete
```
