# Networking and Web - Exercises

## Exercise 1: Weather API Client
Create a client that fetches weather data for a city.

```python
def get_weather(city, api_key):
    """
    Get current weather for a city.

    Args:
        city: City name
        api_key: API key

    Returns:
        Dict with temperature, humidity, description
    """
    pass
```

## Exercise 2: URL Shortener API
Build a simple URL shortener client.

```python
class URLShortener:
    def shorten(self, url):
        """Shorten a URL."""
        pass

    def expand(self, short_url):
        """Expand a shortened URL."""
        pass
```

## Exercise 3: Batch API Requests
Process multiple API requests in batches to respect rate limits.

```python
def batch_requests(urls, batch_size=5, delay=1):
    """
    Make requests in batches.

    Args:
        urls: List of URLs
        batch_size: Requests per batch
        delay: Seconds between batches

    Returns:
        List of responses
    """
    pass
```

## Exercise 4: JSON Data Validator
Validate JSON response against expected schema.

```python
def validate_response(response, schema):
    """
    Validate JSON response.

    Args:
        response: requests.Response object
        schema: Dict defining expected structure

    Returns:
        bool: True if valid
    """
    pass
```

## Exercise 5: API Response Cache
Implement caching for API responses.

```python
class APICache:
    def __init__(self, ttl=300):
        """Initialize cache with TTL in seconds."""
        pass

    def get(self, url):
        """Get cached response or None."""
        pass

    def set(self, url, response):
        """Cache response."""
        pass
```

## Exercise 6: Download Progress Bar
Download file with progress indication.

```python
def download_with_progress(url, filename):
    """
    Download file showing progress.

    Args:
        url: File URL
        filename: Output filename
    """
    pass
```

## Exercise 7: API Rate Limit Handler
Handle API rate limits automatically.

```python
class RateLimitedClient:
    def __init__(self, calls_per_minute=60):
        pass

    def request(self, url):
        """Make rate-limited request."""
        pass
```

## Exercise 8: Parallel Downloads
Download multiple files concurrently.

```python
def parallel_download(urls, output_dir):
    """
    Download multiple files in parallel.

    Args:
        urls: List of URLs
        output_dir: Output directory

    Returns:
        List of downloaded filenames
    """
    pass
```

## Exercise 9: REST API Wrapper
Create a wrapper for a REST API.

```python
class APIClient:
    def __init__(self, base_url, api_key):
        pass

    def get(self, endpoint, params=None):
        pass

    def post(self, endpoint, data=None):
        pass

    def put(self, endpoint, data=None):
        pass

    def delete(self, endpoint):
        pass
```

## Exercise 10: Webhook Server
Implement a simple webhook receiver.

```python
def start_webhook_server(port, callback):
    """
    Start webhook server.

    Args:
        port: Port to listen on
        callback: Function to call with webhook data
    """
    pass
```
