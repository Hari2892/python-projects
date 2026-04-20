import requests

# API with parameters

url = "https://api.github.com/search/repositories"

params = {
    "q": "flask",
    "sort": "stars"
}

response = requests.get(url, params=params)

data = response.json()

print(data["total_count"])