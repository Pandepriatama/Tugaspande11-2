import requests

api_key = 'a887f9c1-370f-4bd4-98e6-cabcbdcc1f9b'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)