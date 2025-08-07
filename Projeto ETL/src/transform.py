import pandas as pd
import json
import os

# carregando dados brutos na bronze
with open(os.path.join('data', 'bronze', 'countries.json'), 'r') as f:
    data = json.load(f)

# Processar dados
processed_data = []
for country in data:
   # Pega o primeiro capital ou vazio
   capital = country.get('capital', [''])[0]
   languages = list(country.get('languages', {}).values())
   num_languages = len(languages)

   processed_data.append({
    "capital": capital,
    "num_languages": num_languages,
    "languages": languages
    })
   
#salvar dados processados
df=pd.DataFrame(processed_data)
df.to_parquet(os.path.join('data', 'silver', 'countries.parquet'))
