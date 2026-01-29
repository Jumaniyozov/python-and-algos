# Networking and Web - Tips and Best Practices

## Essential Best Practices

### 1. Always Use Timeouts

**Bad**:
```python
response = requests.get(url)  # Can hang forever!
```

**Good**:
```python
response = requests.get(url, timeout=5)  # 5 second timeout
```

### 2. Use Sessions for Multiple Requests

**Bad** (creates new connection each time):
```python
for url in urls:
    response = requests.get(url)
```

**Good** (reuses connection):
```python
with requests.Session() as session:
    for url in urls:
        response = session.get(url)
```

### 3. Handle Errors Properly

**Bad**:
```python
response = requests.get(url)
data = response.json()  # Might fail!
```

**Good**:
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Check status
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### 4. Check Status Codes

**Best Practice**:
```python
response = requests.get(url)

if response.status_code == 200:
    # Success
    pass
elif response.status_code == 404:
    # Not found
    pass
elif response.status_code == 429:
    # Rate limited
    pass
else:
    response.raise_for_status()
```

### 5. Respect Rate Limits

```python
import time

def rate_limited_requests(urls, requests_per_second=2):
    delay = 1.0 / requests_per_second
    for url in urls:
        response = requests.get(url)
        yield response
        time.sleep(delay)
```

## Common Pitfalls

### 1. Forgetting to Close Connections

**Bad**:
```python
session = requests.Session()
# ... use session ...
# Never closed!
```

**Good**:
```python
with requests.Session() as session:
    # ... use session ...
# Automatically closed
```

### 2. Not Handling Redirects

```python
# By default, follows redirects
response = requests.get(url, allow_redirects=True)

# Disable if needed
response = requests.get(url, allow_redirects=False)
```

### 3. Ignoring SSL Warnings

**Very Bad** (security risk):
```python
requests.get(url, verify=False)  # Disables SSL verification!
```

**Good**:
```python
requests.get(url)  # Verify SSL by default
```

### 4. Not Setting User-Agent

```python
# Some sites block default user agents
headers = {'User-Agent': 'MyApp/1.0 (contact@example.com)'}
response = requests.get(url, headers=headers)
```

## Performance Tips

### 1. Use streaming for Large Files

```python
# Bad: Loads entire file in memory
response = requests.get(url)
with open('file.zip', 'wb') as f:
    f.write(response.content)

# Good: Streams chunks
response = requests.get(url, stream=True)
with open('file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

### 2. Reuse Connections with Session

```python
session = requests.Session()
# Connection pooling and persistence
for _ in range(100):
    session.get('https://api.example.com/data')
```

### 3. Use Async for Many Requests

```python
import aiohttp
import asyncio

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses
```

## Security Best Practices

### 1. Never Hardcode API Keys

**Bad**:
```python
API_KEY = "sk_live_123456789"  # In source code!
```

**Good**:
```python
import os
API_KEY = os.environ.get('API_KEY')
```

### 2. Validate SSL Certificates

```python
# Always verify SSL (default)
response = requests.get('https://api.example.com')
```

### 3. Sanitize User Input in URLs

```python
from urllib.parse import quote

user_input = "file with spaces.txt"
safe_input = quote(user_input)
url = f"https://api.example.com/files/{safe_input}"
```

## Debugging Tips

### 1. Print Request Details

```python
response = requests.get(url)
print(f"URL: {response.url}")
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Body: {response.text[:200]}")
```

### 2. Use httpbin for Testing

```python
# Test GET
response = requests.get('https://httpbin.org/get')

# Test POST
response = requests.post('https://httpbin.org/post', json={'key': 'value'})

# Test status codes
response = requests.get('https://httpbin.org/status/404')
```

### 3. Enable Request Logging

```python
import logging
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
```

## Common Patterns

### Retry with Exponential Backoff

```python
import time

def retry_request(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return requests.get(url, timeout=5)
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

### Circuit Breaker Pattern

```python
import time

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure = None
        self.state = 'closed'

    def call(self, func, *args, **kwargs):
        if self.state == 'open':
            if time.time() - self.last_failure > self.timeout:
                self.state = 'half-open'
            else:
                raise Exception("Circuit breaker is open")

        try:
            result = func(*args, **kwargs)
            if self.state == 'half-open':
                self.state = 'closed'
                self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure = time.time()
            if self.failures >= self.failure_threshold:
                self.state = 'open'
            raise
```

## Quick Reference

**GET request**:
```python
requests.get(url, params={'key': 'value'}, timeout=5)
```

**POST with JSON**:
```python
requests.post(url, json={'key': 'value'}, timeout=5)
```

**Custom headers**:
```python
headers = {'Authorization': 'Bearer token'}
requests.get(url, headers=headers)
```

**Download file**:
```python
response = requests.get(url, stream=True)
with open('file', 'wb') as f:
    for chunk in response.iter_content(8192):
        f.write(chunk)
```

**Error handling**:
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
