import urllib.request
import json

# Basic API request (using built-in urllib)
url = "https://api.github.com/users/python"
try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        print(data["login"])
        print(data["public_repos"])
except Exception as e:
    print(f"Error: {e}")

# Note: For real projects, install requests:
# pip install requests

"""
import requests

response = requests.get("https://api.github.com/users/python")
print(response.status_code)
data = response.json()

# With parameters
params = {"q": "python", "page": 1}
response = requests.get("https://api.github.com/search/repositories", params=params)

# POST request
payload = {"name": "test", "value": 123}
response = requests.post("https://httpbin.org/post", json=payload)
"""
