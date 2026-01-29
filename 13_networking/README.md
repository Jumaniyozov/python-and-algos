# Chapter 13: Networking and Web

Master Python's networking capabilities and web interaction tools.

## What You'll Learn

- socket programming basics
- HTTP clients (urllib, requests)
- JSON and API interaction
- Email handling (smtplib, email)
- Error handling and retries
- Real-world networking patterns

## Files

- [theory.md](theory.md) - Networking fundamentals
- [examples.md](examples.md) - Practical examples
- [exercises.md](exercises.md) - Practice problems
- [solutions.md](solutions.md) - Solutions
- [tips.md](tips.md) - Best practices

## Quick Reference

### HTTP GET Request
```python
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
```

### POST with JSON
```python
response = requests.post(
    'https://api.example.com/users',
    json={'name': 'Alice', 'email': 'alice@example.com'}
)
```

### Error Handling
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Prerequisites

- Basic Python syntax
- Understanding of HTTP protocol
- JSON knowledge

## Next Steps

- Chapter 12: Concurrency (async networking)
- REST API development
- Web scraping techniques
