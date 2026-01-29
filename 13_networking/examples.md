# Networking and Web - Examples

## Example 1: Basic GET Request with requests

```python
import requests

# Simple GET request
response = requests.get('https://api.github.com')
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers['content-type']}")
print(f"Body: {response.text[:100]}...")

# GET with parameters
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)
data = response.json()
print(f"Found {data['total_count']} repositories")
```

## Example 2: POST Request with JSON

```python
import requests

# POST with JSON data
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'My Post',
    'body': 'This is the content',
    'userId': 1
}

response = requests.post(url, json=data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
```

## Example 3: Error Handling

```python
import requests
from requests.exceptions import RequestException, Timeout, HTTPError

def safe_request(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise HTTPError for bad status
        return response.json()
    except Timeout:
        print(f"Request timed out after {timeout}s")
    except HTTPError as e:
        print(f"HTTP error: {e}")
    except RequestException as e:
        print(f"Request failed: {e}")
    return None

# Test
data = safe_request('https://api.github.com/users/octocat')
if data:
    print(f"User: {data['name']}")
```

## Example 4: Using Sessions

```python
import requests

# Session maintains connection and cookies
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Multiple requests reuse connection
response1 = session.get('https://httpbin.org/cookies/set/session/123')
response2 = session.get('https://httpbin.org/cookies')
print(response2.json())  # Shows session cookie

session.close()

# Or use context manager
with requests.Session() as session:
    response = session.get('https://api.github.com')
# Automatically closed
```

## Example 5: Download File

```python
import requests

def download_file(url, filename):
    """Download file with progress."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            if total_size:
                percent = (downloaded / total_size) * 100
                print(f"Downloaded: {percent:.1f}%", end='\r')

    print(f"\nSaved to {filename}")

# Download a file
download_file('https://httpbin.org/image/png', 'test.png')
```

## Example 6: API Client Class

```python
import requests

class GitHubAPI:
    BASE_URL = 'https://api.github.com'

    def __init__(self, token=None):
        self.session = requests.Session()
        if token:
            self.session.headers.update({'Authorization': f'token {token}'})

    def get_user(self, username):
        """Get user information."""
        response = self.session.get(f'{self.BASE_URL}/users/{username}')
        response.raise_for_status()
        return response.json()

    def get_repos(self, username):
        """Get user repositories."""
        response = self.session.get(f'{self.BASE_URL}/users/{username}/repos')
        response.raise_for_status()
        return response.json()

# Usage
api = GitHubAPI()
user = api.get_user('octocat')
print(f"{user['name']}: {user['public_repos']} repos")

repos = api.get_repos('octocat')
for repo in repos[:5]:
    print(f"- {repo['name']}: {repo['stargazers_count']} stars")
```

## Example 7: Retry with Exponential Backoff

```python
import requests
import time

def request_with_retry(url, max_retries=3, backoff_factor=2):
    """Request with exponential backoff retry."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = backoff_factor ** attempt
            print(f"Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
            time.sleep(wait_time)

# Test
response = request_with_retry('https://api.github.com/rate_limit')
print(response.json())
```

## Example 8: Handle Pagination

```python
import requests

def get_all_repos(username):
    """Get all repos handling pagination."""
    repos = []
    url = f'https://api.github.com/users/{username}/repos'

    while url:
        response = requests.get(url, params={'per_page': 100})
        response.raise_for_status()
        repos.extend(response.json())

        # Check for next page
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    return repos

# Usage
repos = get_all_repos('torvalds')
print(f"Total repos: {len(repos)}")
```

## Example 9: JSON Parsing

```python
import json
import requests

# Get JSON data
response = requests.get('https://api.github.com/users/octocat')
data = response.json()  # Automatic JSON parsing

# Manual JSON parsing
json_str = response.text
data = json.loads(json_str)

# Pretty print JSON
print(json.dumps(data, indent=2))

# Save to file
with open('user.json', 'w') as f:
    json.dump(data, f, indent=2)

# Load from file
with open('user.json', 'r') as f:
    loaded_data = json.load(f)
```

## Example 10: Rate Limiting

```python
import requests
import time
from datetime import datetime

class RateLimiter:
    def __init__(self, calls_per_second):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0

    def wait(self):
        """Wait if necessary to respect rate limit."""
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()

# Usage
limiter = RateLimiter(calls_per_second=2)

for i in range(5):
    limiter.wait()
    response = requests.get('https://api.github.com')
    print(f"{datetime.now().strftime('%H:%M:%S')}: Request {i+1}")
```

## Example 11: Basic Socket Server and Client

```python
import socket

# Server
def start_server(host='localhost', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(data)  # Echo back

# Client
def start_client(host='localhost', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, server!')
        data = s.recv(1024)
        print(f"Received: {data.decode()}")

# Run server in one terminal, client in another
```

## Example 12: HTTP Headers

```python
import requests

# Custom headers
headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer YOUR_TOKEN_HERE'
}

response = requests.get('https://api.github.com/user', headers=headers)

# View request headers
print("Request headers:")
print(response.request.headers)

# View response headers
print("\nResponse headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
```

## Example 13: Query Parameters

```python
import requests

# Method 1: URL with parameters
url = 'https://api.github.com/search/repositories?q=python&sort=stars'
response = requests.get(url)

# Method 2: Pass params dict (preferred)
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 5
}
response = requests.get('https://api.github.com/search/repositories', params=params)

# View final URL
print(f"Final URL: {response.url}")

data = response.json()
for repo in data['items']:
    print(f"{repo['full_name']}: {repo['stargazers_count']} stars")
```

## Example 14: Upload File

```python
import requests

# Upload file
def upload_file(url, filepath):
    with open(filepath, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        return response.json()

# Upload multiple files
files = {
    'file1': open('doc1.txt', 'rb'),
    'file2': open('doc2.txt', 'rb')
}
response = requests.post('https://httpbin.org/post', files=files)
print(response.json())
```

## Example 15: Webhook Handler

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        print(f"Received webhook: {data}")

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'status': 'received'})
        self.wfile.write(response.encode())

# Start server
server = HTTPServer(('localhost', 8000), WebhookHandler)
print("Webhook server running on port 8000")
server.serve_forever()
```
