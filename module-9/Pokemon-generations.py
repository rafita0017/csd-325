import requests

url = 'https://pokeapi.co/api/v2/generation/?limit=2'
response = requests.get(url)

print("Raw response from PokéAPI:")
print(response.text)

print("\nFormatted output:")
data = response.json()

for generation in data['results']:
    name = generation['name']
    link = generation['url']
    print(f"{name.title()} - {link}")