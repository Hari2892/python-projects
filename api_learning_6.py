import requests

# Always handle errors

try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)