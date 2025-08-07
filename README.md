🚀 Evoluindo meu aprendizado em Arquitetura de Dados com o Projeto Medalhão! 🏗️

Estou animado para compartilhar meu mais recente projeto, onde implementei uma arquitetura de dados em camadas (Bronze → Silver → Gold) para manipulação e visualização de dados de países.
Este projeto não só me ajudou a aprofundar meus conhecimentos em ETL (Extração, Transformação e Carga), mas também a trabalhar com ferramentas modernas de análise de dados.

🔗Fases do Projeto:
Camada Bronze — Raw / Bruta:

Extração: Coletamos dados diretamente da API restcountries.com e os salvamos em formato JSON, sem modificações.
Bibliotecas Utilizadas: requests, json
Exemplo de entrada:
{
"capital": ["Beijing"],
...
Camada Silver — Limpeza e Padronização:

Transformação: Utilizando Python e Pandas, extraímos a capital como string, convertendo os idiomas para uma lista e calculando o número de idiomas falados.
Dados salvos em formato Parquet: Um formato colunar otimizado para armazenamento.
Bibliotecas Utilizadas: pandas, pyarrow
Exemplo de saída:
{
"capital": "Beijing",
...
Camada Gold — Agregações e Insights:

Visões Analíticas: Criamos duas visualizações:
languages_most_spoken.parquet: Idiomas mais falados.
capitals_by_language_count.parquet: Capitais com mais idiomas oficiais.
**Dados prontos para visualização e análises de negócio.
Bibliotecas Utilizadas: pandas
📊 Visualização com Streamlit:

Desenvolvi um dashboard interativo que permite visualizar os idiomas mais falados e as capitais com mais idiomas oficiais, além de interagir com os dados em tempo real.
Biblioteca Utilizada: streamlit
Ferramentas Utilizadas:
Extração: requests, json
Transformação: pandas, pyarrow
Armazenamento: .parquet (colunar)
Visualização: streamlit
