# Chapter 24: Web Development

## Overview

This chapter introduces web development fundamentals in Python, covering HTTP concepts, REST APIs, and modern web frameworks. You'll learn to build backend services, handle requests, and create scalable web applications.

## What You'll Learn

- **HTTP & Requests**: Understanding web protocols and making HTTP requests
- **REST APIs**: Designing and consuming RESTful web services
- **Flask**: Lightweight web framework for building applications
- **FastAPI**: Modern async web framework with automatic documentation
- **Web Patterns**: Request/response cycles, routing, middleware
- **Data Validation**: Input validation and error handling

## Why It Matters

Web development is essential for:
- Building backend services and APIs
- Creating web applications and services
- Integrating with external services
- Understanding HTTP and web protocols
- Building microservices and distributed systems

## Prerequisites

- Python fundamentals (Chapters 1-7)
- Functions and modules (Chapter 6)
- Object-oriented programming basics (Chapter 7)
- JSON handling (Chapter 12)
- Decorators understanding (Chapter 9)

## Installation

```bash
# Install required packages
pip install requests flask fastapi uvicorn

# For development
pip install pytest httpx
```

## Chapter Structure

1. **Theory** (`theory.md`): Core concepts and fundamentals
2. **Examples** (`examples.md`): 15 practical, runnable examples
3. **Exercises** (`exercises.md`): 15 progressive challenges
4. **Solutions** (`solutions.md`): Detailed solutions with explanations
5. **Tips** (`tips.md`): Best practices and common patterns

## Quick Start

### Making HTTP Requests

```python
import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())

# POST request
data = {'title': 'New Post', 'body': 'Content', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
```

### Simple Flask API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    return jsonify({'id': 1, **data}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    body: str
    userId: int

@app.get('/hello')
def hello():
    return {'message': 'Hello, World!'}

@app.post('/posts')
def create_post(post: Post):
    return {'id': 1, **post.dict()}
```

## Real-World Applications

- RESTful APIs and microservices
- Web scraping and integration
- Data fetching and processing
- Backend for mobile and web apps
- Real-time notification systems
- Rate-limited API interactions

## Key Takeaways

By the end of this chapter, you'll be able to:
1. Make HTTP requests with the requests library
2. Build REST APIs with Flask
3. Create modern async APIs with FastAPI
4. Handle JSON data and validation
5. Design and implement web endpoints
6. Handle errors and edge cases
7. Document and test APIs

## Next Steps

After mastering this chapter:
- Explore database integration (SQLAlchemy, SQLModel)
- Learn authentication and security (JWT, OAuth)
- Study async programming (asyncio, aiohttp)
- Master testing frameworks (pytest, httpx)
- Deploy to production (Heroku, AWS, Docker)

---

**Time to Complete**: 8-10 hours
**Difficulty**: Intermediate to Advanced
**Practice Projects**: 3-5 complete API projects recommended
