import requests

# Basic API Call (GET request)

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)