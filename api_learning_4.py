import requests

# POST request (send data)

url = "https://httpbin.org/post"

payload = {
    "name": "user",
    "language": "python"
}

response = requests.post(url, json=payload)

print(response.json())