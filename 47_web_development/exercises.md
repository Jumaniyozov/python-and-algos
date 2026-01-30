# Web Development - Exercises

## 15 Progressive Challenges

### Requests Library Exercises

#### Exercise 1: GET Request Basics

Use the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) to:
1. Fetch a single post (id=1) and print the title
2. Fetch all posts for a specific user (userId=2)
3. Print the number of posts retrieved
4. Extract and display the first post's body

**Expected Output:**
```
Post 1 title: sunt aut facere repellat provident...
Retrieved 10 posts for userId 2
First post body: quia enim...
```

#### Exercise 2: POST and PUT Requests

Using JSONPlaceholder:
1. Create a new post with title and body
2. Update post id=1 with new data
3. Print the response from both requests
4. Verify the status codes are correct

**Hint:** Use `requests.post()` and `requests.put()`

#### Exercise 3: Query Parameters and Filtering

Fetch posts with:
1. Pagination (skip first 5, get next 5)
2. Filter posts by userId
3. Sort results (if API supports)
4. Print count of results

**Hint:** Use `params` argument in requests.get()

#### Exercise 4: Error Handling

Create a robust script that:
1. Tries multiple API endpoints
2. Handles 404 errors gracefully
3. Handles connection timeouts
4. Logs all errors with appropriate messages

**Hint:** Use try-except with specific exception types

#### Exercise 5: Session Management

Create a session that:
1. Makes multiple requests with shared headers
2. Includes authorization token in all requests
3. Logs each request and response
4. Closes session properly

**Hint:** Use `requests.Session()`

---

### Flask Exercises

#### Exercise 6: Simple Flask API

Build a Flask app with:
1. GET /items - list all items
2. GET /items/<id> - get specific item
3. POST /items - create new item
4. Store data in a list (in-memory)

**Requirements:**
- Proper status codes
- JSON responses
- Error handling for missing items

#### Exercise 7: Query Parameters in Flask

Create endpoints:
1. GET /products?category=electronics - filter by category
2. GET /products?minPrice=100&maxPrice=500 - price range
3. GET /products?sortBy=price&order=asc - sorting
4. Combine multiple filters

**Data Structure:**
```python
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 999},
    {'id': 2, 'name': 'Book', 'category': 'books', 'price': 25},
    ...
]
```

#### Exercise 8: Request Body Validation

Build endpoint POST /users:
1. Accept JSON with name, email, age
2. Validate all fields are present
3. Validate email format
4. Validate age is positive integer
5. Return appropriate error messages

**Test Cases:**
- Valid data → 201 Created
- Missing fields → 400 Bad Request
- Invalid email → 400 Bad Request
- Invalid age → 400 Bad Request

#### Exercise 9: Error Handling Decorators

Create decorators:
1. @require_json - ensure Content-Type is JSON
2. @require_auth - ensure Authorization header exists
3. @handle_errors - catch exceptions and return proper status

Implement endpoints using these decorators

#### Exercise 10: Complete CRUD API

Build full CRUD for a resource:
1. Create (POST) - add new item
2. Read (GET) - retrieve item(s)
3. Update (PUT) - replace item
4. Delete (DELETE) - remove item
5. List with filtering and pagination

**Requirements:**
- All proper status codes
- Validation on create/update
- 404 for missing items
- 400 for bad requests

---

### FastAPI Exercises

#### Exercise 11: Basic FastAPI Application

Create FastAPI app with:
1. GET / - welcome message
2. GET /items - list items
3. GET /items/{item_id} - get specific item
4. POST /items - create item
5. Define Pydantic models

**Hint:** Use `from fastapi import FastAPI` and `pydantic.BaseModel`

#### Exercise 12: Type Validation and Query Parameters

Build endpoint with:
1. Path parameter with type checking (int, float, string)
2. Query parameters with defaults
3. Query parameters with validation (min, max values)
4. Optional query parameters

**Example:**
```
GET /search?query=python&minRating=3&maxRating=5&page=1
```

#### Exercise 13: Request Body Validation

Create Pydantic models with:
1. Required fields with type hints
2. Optional fields with defaults
3. Field validation (min_length, max_length, regex, gt, lt)
4. Custom validators

**Example Model:**
```python
class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., regex=r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
    age: int = Field(..., gt=0, le=150)
```

#### Exercise 14: Response Models

Create endpoints with:
1. Different response models for input and output
2. Nested models
3. List responses
4. Model serialization

#### Exercise 15: Complete API with Error Handling

Build complete mini API:
1. Multiple endpoints for different resources
2. Comprehensive error handling with HTTPException
3. Request validation
4. Response models
5. Proper status codes

**Structure:**
- GET /api/resource - list all
- GET /api/resource/{id} - get one
- POST /api/resource - create
- PUT /api/resource/{id} - update
- DELETE /api/resource/{id} - delete

---

## Advanced Challenges

### Challenge A: API Rate Limiting

Implement simple rate limiting in Flask:
- Track requests per IP address
- Limit to 10 requests per minute
- Return 429 status when limit exceeded
- Include X-RateLimit headers in response

### Challenge B: Authentication Token System

Create token-based auth:
- POST /auth/login - generate token
- POST /auth/logout - invalidate token
- GET /protected - requires valid token
- Return 401 for invalid/missing token

### Challenge C: Data Persistence

Integrate SQLite:
- Save/load data from database
- Replace in-memory storage
- Maintain same API interface
- Add database initialization

### Challenge D: Testing Your API

Write tests for your API:
- Test all endpoints
- Test status codes
- Test error cases
- Test validation
- Use pytest and httpx

---

## Testing Endpoints with curl

```bash
# GET
curl http://localhost:5000/items

# POST
curl -X POST http://localhost:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "New Item", "price": 99.99}'

# PUT
curl -X PUT http://localhost:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated", "price": 49.99}'

# DELETE
curl -X DELETE http://localhost:5000/items/1

# With auth header
curl -H "Authorization: Bearer token123" \
  http://localhost:5000/protected

# With query parameters
curl "http://localhost:5000/items?category=books&minPrice=10"
```

---

## Hints for Success

1. **Start simple** - Get basic endpoints working first
2. **Test as you go** - Test each endpoint before moving on
3. **Use curl or Postman** - Test from command line
4. **Print debug info** - Use print() for debugging
5. **Read error messages** - Errors tell you what's wrong
6. **Follow REST principles** - Use correct HTTP methods
7. **Validate input** - Check data before processing
8. **Handle errors gracefully** - Return proper status codes

---

## Challenge Progression

1. **Exercises 1-5**: Requests library fundamentals
2. **Exercises 6-10**: Flask basics and patterns
3. **Exercises 11-15**: FastAPI and modern patterns
4. **Advanced Challenges**: Real-world scenarios

Each exercise builds on previous knowledge. Complete in order for best results.
