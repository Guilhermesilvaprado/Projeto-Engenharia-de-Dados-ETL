import streamlit as st
import pandas as pd
import os

st.title("Dashboard de Países")

# Carregar dados
languages_df = pd.read_parquet(os.path.join(
    'data', 'gold', 'languages_most_spoken.parquet'))
capitals_df = pd.read_parquet(os.path.join(
    'data', 'gold', 'capitals_by_language_count.parquet'))

# Visualizar idiomas mais falados
st.subheader("Idiomas Mais Falados")
st.bar_chart(languages_df.set_index('languages'))

# Gráfico de Barras Horizontal para Idiomas Mais Falados
st.subheader("Idiomas Mais Falados (Gráfico Horizontal)")
st.bar_chart(languages_df.set_index('languages')['count'])

# Visualizar capitais com mais idiomas oficiais
st.subheader("Capitais com Mais Idiomas Oficiais")
st.bar_chart(capitals_df.set_index('capital'))

# Gráfico de Barras Horizontal para Capitais
st.subheader("Capitais com Mais Idiomas Oficiais (Gráfico Horizontal)")
st.bar_chart(capitals_df.set_index('capital')['num_languages'])
