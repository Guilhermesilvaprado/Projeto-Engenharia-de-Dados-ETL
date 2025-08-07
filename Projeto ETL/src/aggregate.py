import pandas as pd
import os

# Carregar dados processados
df = pd.read_parquet(os.path.join('data', 'silver', 'countries.parquet'))

# Idiomas mais falados
languages_most_spoken = df.explode('languages').groupby('languages').size().reset_index(name='count')
languages_most_spoken.to_parquet(os.path.join('data', 'gold', 'languages_most_spoken.parquet'))

# Capitais com mais idiomas oficiais
capitals_by_language_count = df.groupby('capital')['num_languages'].max().reset_index()
capitals_by_language_count.to_parquet(os.path.join('data', 'gold', 'capitals_by_language_count.parquet'))
