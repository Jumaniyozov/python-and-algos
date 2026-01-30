# Web Development - Examples

## 15 Practical, Runnable Examples

### Requests Library Examples

#### Example 1: Simple GET Request

```python
import requests

# Get data from public API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

# Output:
# Status Code: 200
# Response JSON:
# {
#   'userId': 1,
#   'id': 1,
#   'title': 'sunt aut facere repellat...',
#   'body': 'quia et suscipit...'
# }
```

#### Example 2: POST Request with Data

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# Create new post
data = {
    'title': 'New Post Title',
    'body': 'This is the post body content.',
    'userId': 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Created Post:")
print(response.json())

# Output:
# Status Code: 201
# Created Post:
# {'userId': 1, 'id': 101, 'title': 'New Post Title', 'body': '...'}
```

#### Example 3: Query Parameters

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# Get posts with pagination
params = {'_page': 1, '_limit': 5}
response = requests.get(url, params=params)

posts = response.json()
print(f"Retrieved {len(posts)} posts")
for post in posts[:2]:
    print(f"  - {post['title'][:40]}...")

# Output:
# Retrieved 5 posts
#   - sunt aut facere repellat provident...
#   - qui est esse...
```

#### Example 4: Headers and Authentication

```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer sample-token-123'
}

response = requests.get(
    'https://jsonplaceholder.typicode.com/posts/1',
    headers=headers
)

print("Headers sent:")
for key, value in headers.items():
    print(f"  {key}: {value}")

print(f"\nResponse Status: {response.status_code}")
```

#### Example 5: Error Handling

```python
import requests

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/999999',  # Not found
    'https://invalid-url-that-does-not-exist.com',  # Connection error
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for bad status
        print(f"✓ {url}: {response.status_code}")
    except requests.exceptions.HTTPError as e:
        print(f"✗ {url}: HTTP Error {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"✗ {url}: Connection failed")
    except requests.exceptions.Timeout:
        print(f"✗ {url}: Request timed out")

# Output:
# ✓ https://jsonplaceholder.typicode.com/posts/1: 200
# ✗ https://jsonplaceholder.typicode.com/posts/999999: HTTP Error 404
# ✗ https://invalid-url...: Connection failed
```

#### Example 6: Session Management

```python
import requests

# Create session to reuse headers and cookies
session = requests.Session()
session.headers.update({
    'Authorization': 'Bearer sample-token',
    'User-Agent': 'MyApp/1.0'
})

# Multiple requests share session headers and cookies
response1 = session.get('https://jsonplaceholder.typicode.com/posts/1')
response2 = session.get('https://jsonplaceholder.typicode.com/posts/2')

print(f"Request 1 status: {response1.status_code}")
print(f"Request 2 status: {response2.status_code}")

# Close session when done
session.close()

# Or use context manager
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token'})
    response = session.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"Status: {response.status_code}")
```

---

### Flask Examples

#### Example 7: Basic Flask API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
posts = [
    {'id': 1, 'title': 'First Post', 'body': 'Content...'},
    {'id': 2, 'title': 'Second Post', 'body': 'More content...'}
]

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to Flask API'})

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400

    new_post = {
        'id': max(p['id'] for p in posts) + 1,
        'title': data['title'],
        'body': data.get('body', '')
    }
    posts.append(new_post)
    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### Example 8: Flask with Query Parameters

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Item A', 'category': 'tools', 'price': 50},
    {'id': 2, 'name': 'Item B', 'category': 'tools', 'price': 75},
    {'id': 3, 'name': 'Item C', 'category': 'books', 'price': 25},
]

@app.route('/items', methods=['GET'])
def list_items():
    # Get query parameters
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    limit = request.args.get('limit', 10, type=int)

    # Filter
    result = items
    if category:
        result = [i for i in result if i['category'] == category]
    if min_price:
        result = [i for i in result if i['price'] >= min_price]

    # Limit
    result = result[:limit]

    return jsonify({'items': result, 'count': len(result)})

if __name__ == '__main__':
    app.run(debug=True)

# Test:
# curl "http://localhost:5000/items"
# curl "http://localhost:5000/items?category=tools"
# curl "http://localhost:5000/items?min_price=30"
# curl "http://localhost:5000/items?category=tools&min_price=60"
```

#### Example 9: Flask Error Handling

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Resource not found',
        'status_code': 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'status_code': 500
    }), 500

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({
            'error': 'Division by zero',
            'status_code': 400
        }), 400
    return jsonify({
        'result': a / b,
        'a': a,
        'b': b
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id < 1:
        return jsonify({
            'error': 'Invalid user ID',
            'status_code': 400
        }), 400
    return jsonify({'id': user_id, 'name': f'User {user_id}'})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Example 10: Flask Decorators for Authentication

```python
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def require_auth(f):
    """Decorator to require Authorization header"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Missing authorization header'}), 401
        if not token.startswith('Bearer '):
            return jsonify({'error': 'Invalid token format'}), 401
        return f(*args, **kwargs)
    return decorated_function

def require_json(f):
    """Decorator to require JSON content type"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        return f(*args, **kwargs)
    return decorated_function

@app.route('/public', methods=['GET'])
def public_endpoint():
    return jsonify({'message': 'Public data'})

@app.route('/protected', methods=['GET'])
@require_auth
def protected_endpoint():
    token = request.headers.get('Authorization').split(' ')[1]
    return jsonify({'message': 'Protected data', 'token': token})

@app.route('/create', methods=['POST'])
@require_json
@require_auth
def create_resource():
    data = request.json
    return jsonify({'created': True, 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

---

### FastAPI Examples

#### Example 11: Basic FastAPI Application

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str
    userId: int

posts = [
    {'id': 1, 'title': 'First Post', 'body': 'Content...', 'userId': 1},
    {'id': 2, 'title': 'Second Post', 'body': 'More...', 'userId': 1}
]

@app.get('/')
def read_root():
    return {'message': 'Welcome to FastAPI'}

@app.get('/posts')
def list_posts():
    return {'posts': posts}

@app.get('/posts/{post_id}')
def get_post(post_id: int):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return {'error': 'Post not found'}, 404
    return post

@app.post('/posts')
def create_post(post: Post):
    new_id = max(p['id'] for p in posts) + 1
    new_post = {'id': new_id, **post.dict()}
    posts.append(new_post)
    return new_post

# Run with: uvicorn filename:app --reload
```

#### Example 12: FastAPI with Query Parameters and Validation

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items = [
    {'id': 1, 'name': 'Item A', 'price': 50},
    {'id': 2, 'name': 'Item B', 'price': 75},
]

@app.get('/items')
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: str = None
):
    """
    Query parameters with validation:
    - skip: offset (>=0)
    - limit: number of items (1-100)
    - name: optional filter by name
    """
    result = items
    if name:
        result = [i for i in result if name.lower() in i['name'].lower()]
    return {
        'items': result[skip:skip+limit],
        'total': len(result)
    }

@app.post('/items')
def create_item(item: Item):
    new_item = {
        'id': max(i.get('id', 0) for i in items) + 1,
        **item.dict()
    }
    items.append(new_item)
    return new_item

# Test: http://localhost:8000/items?skip=0&limit=5
# Test: http://localhost:8000/items?name=Item
```

#### Example 13: FastAPI Response Models

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PostCreate(BaseModel):
    title: str
    body: str

class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    author: str

posts_db = [
    {'id': 1, 'title': 'First', 'body': 'Content', 'author': 'Alice'},
]

@app.get('/posts', response_model=List[PostResponse])
def list_posts():
    return posts_db

@app.get('/posts/{post_id}', response_model=PostResponse)
def get_post(post_id: int):
    for post in posts_db:
        if post['id'] == post_id:
            return post
    return {'error': 'Not found'}, 404

@app.post('/posts', response_model=PostResponse)
def create_post(post: PostCreate):
    new_post = {
        'id': len(posts_db) + 1,
        **post.dict(),
        'author': 'Anonymous'
    }
    posts_db.append(new_post)
    return new_post
```

#### Example 14: FastAPI Error Handling

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/divide/{a}/{b}')
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail='Division by zero error'
        )
    return {'result': a / b}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(
            status_code=400,
            detail='User ID must be positive'
        )
    if user_id > 1000:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    return {'id': user_id, 'name': f'User {user_id}'}

@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    if item_id not in [1, 2, 3]:
        raise HTTPException(
            status_code=404,
            detail=f'Item {item_id} not found'
        )
    return {'message': f'Item {item_id} deleted'}
```

#### Example 15: FastAPI with Path and Body Parameters

```python
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Review(BaseModel):
    rating: int
    comment: str

@app.put('/items/{item_id}')
def update_item(
    item_id: int = Path(..., gt=0, lt=100),
    item_name: str = Body(...),
    review: Review = Body(None)
):
    """
    Update item with validation:
    - item_id: 1-99
    - item_name: required in body
    - review: optional review in body
    """
    return {
        'item_id': item_id,
        'item_name': item_name,
        'review': review
    }

# POST /items/5
# {
#   "item_name": "Updated Item",
#   "review": {
#     "rating": 5,
#     "comment": "Great!"
#   }
# }
```

---

## Example Integration: Complete Mini API

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory database
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

posts = [
    {'id': 1, 'userId': 1, 'title': 'First Post', 'body': 'Content...', 'created': '2024-01-01'},
    {'id': 2, 'userId': 1, 'title': 'Second Post', 'body': 'More...', 'created': '2024-01-02'}
]

# User endpoints
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not all(k in data for k in ['name', 'email']):
        return jsonify({'error': 'Missing fields'}), 400

    new_user = {
        'id': max(u['id'] for u in users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Post endpoints
@app.route('/posts', methods=['GET'])
def get_posts():
    user_id = request.args.get('userId', type=int)
    result = posts
    if user_id:
        result = [p for p in posts if p['userId'] == user_id]
    return jsonify({'posts': result})

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    required = ['userId', 'title', 'body']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400

    new_post = {
        'id': max(p['id'] for p in posts) + 1,
        'userId': data['userId'],
        'title': data['title'],
        'body': data['body'],
        'created': datetime.now().isoformat()
    }
    posts.append(new_post)
    return jsonify(new_post), 201

if __name__ == '__main__':
    app.run(debug=True)
```

Test with curl:
```bash
curl http://localhost:5000/users
curl http://localhost:5000/posts?userId=1
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"userId":1,"title":"Test","body":"Content"}'
```
