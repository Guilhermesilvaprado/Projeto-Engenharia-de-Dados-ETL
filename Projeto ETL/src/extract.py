import requests
import json
import os

url = "https://restcountries.com/v3.1/independent?status=true&fields=languages,capital"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open(os.path.join('data', 'bronze', 'countries.json'), 'w') as f:
        json.dump(data, f)
else:
    print(f"Erro ao acessar a API: {response.status_code}")
