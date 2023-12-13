import requests
url = "https://anapioficeandfire.com/api/characters/583"
response = requests.get(url)
data = response.json()
print(data)