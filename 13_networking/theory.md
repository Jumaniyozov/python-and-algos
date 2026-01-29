# Networking and Web - Theory

## Core Concepts

### 1. Network Layers

**OSI Model (simplified)**:
- Application Layer: HTTP, FTP, SMTP (what we work with)
- Transport Layer: TCP, UDP
- Network Layer: IP
- Physical Layer: Hardware

### 2. Sockets

**What are Sockets?**:
- Endpoints for network communication
- Identified by IP address + port number
- Two types: TCP (reliable) and UDP (fast, unreliable)

**Socket Workflow**:
1. Create socket
2. Bind to address/port (server)
3. Listen for connections (server)
4. Accept connections (server) or Connect (client)
5. Send/Receive data
6. Close socket

### 3. HTTP Protocol

**Request Components**:
- Method: GET, POST, PUT, DELETE, etc.
- URL: Resource location
- Headers: Metadata (content-type, authorization, etc.)
- Body: Data (for POST/PUT)

**Response Components**:
- Status Code: 200 OK, 404 Not Found, 500 Error, etc.
- Headers: Metadata
- Body: Content

**Common Status Codes**:
- 2xx: Success (200 OK, 201 Created)
- 3xx: Redirection (301 Moved, 302 Found)
- 4xx: Client Error (400 Bad Request, 404 Not Found, 429 Too Many Requests)
- 5xx: Server Error (500 Internal Error, 503 Unavailable)

### 4. urllib vs requests

**urllib (built-in)**:
- Standard library
- More verbose
- Lower-level control
- No external dependencies

**requests (third-party)**:
- Much more Pythonic
- Simpler API
- Better features (sessions, automatic JSON)
- Industry standard (`pip install requests`)

### 5. REST APIs

**Principles**:
- Stateless: Each request independent
- Resource-based: URLs represent resources
- Standard methods: GET (read), POST (create), PUT (update), DELETE (delete)
- JSON: Common data format

**Best Practices**:
- Use appropriate HTTP methods
- Return proper status codes
- Version APIs (/v1/, /v2/)
- Handle errors consistently

### 6. JSON

**What is JSON?**:
- JavaScript Object Notation
- Text-based data format
- Language-independent
- Human-readable

**Python Integration**:
```python
import json

# Serialize (Python → JSON)
json_str = json.dumps({'name': 'Alice', 'age': 30})

# Deserialize (JSON → Python)
data = json.loads(json_str)
```

### 7. Error Handling

**Network Errors**:
- ConnectionError: Can't connect
- Timeout: Request too slow
- HTTPError: Bad status code
- RequestException: Base exception

**Retry Strategy**:
- Exponential backoff
- Maximum retry attempts
- Idempotent requests only (GET, PUT, DELETE)

## Common Patterns

### API Client Pattern
```python
class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def get(self, endpoint):
        return self.session.get(f'{self.base_url}/{endpoint}').json()
```

### Retry with Exponential Backoff
```python
import time

def retry_request(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return requests.get(url)
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # 1s, 2s, 4s
```

### Pagination Handler
```python
def get_all_pages(base_url):
    page = 1
    while True:
        response = requests.get(f'{base_url}?page={page}')
        data = response.json()
        yield data['results']
        if not data.get('next'):
            break
        page += 1
```

## Best Practices

1. **Use timeouts**: Prevent hanging requests
2. **Handle errors**: Network always unreliable
3. **Use sessions**: Reuse connections
4. **Respect rate limits**: Add delays between requests
5. **Validate responses**: Check status codes
6. **Use HTTPS**: Security first
7. **Set User-Agent**: Identify your application
8. **Cache when possible**: Reduce API calls
