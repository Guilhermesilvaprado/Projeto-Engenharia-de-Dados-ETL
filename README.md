# 🏗️ Projeto Medalhão — Arquitetura de Dados em Camadas

🚀 Evoluindo meu aprendizado em Arquitetura de Dados com o Projeto Medalhão! Este projeto implementa uma arquitetura em camadas (Bronze → Silver → Gold) para manipulação e visualização de dados de países, utilizando a API [restcountries.com](https://restcountries.com). Além de consolidar conceitos de ETL (Extração, Transformação e Carga), o projeto explora ferramentas modernas de análise e visualização de dados.

Na camada Bronze, os dados são coletados diretamente da API e salvos em formato JSON, sem modificações. Utilizei as bibliotecas `requests` e `json` para essa etapa. Um exemplo de entrada seria:

```json
{
  "capital": ["Beijing"],
  "languages": {
    "zh": "Chinese"
  }
}
Na camada Silver, os dados passam por limpeza e padronização. Com pandas e pyarrow, converti a capital para string, transformei os idiomas em uma lista e calculei o número de idiomas falados. Os dados foram salvos em formato .parquet, que é colunar e otimizado para armazenamento. Um exemplo de saída seria

```json
{
  "capital": "Beijing",
  "languages": ["Chinese"],
  "language_count": 1
}

Na camada Gold, foram geradas visões analíticas com foco em insights. Criei dois arquivos: languages_most_spoken.parquet, que mostra os idiomas mais falados, e capitals_by_language_count.parquet, que apresenta as capitais com mais idiomas oficiais. Tudo pronto para visualização e análises de negócio.
Para a visualização, desenvolvi um dashboard interativo com streamlit, que permite explorar os idiomas mais falados e as capitais com mais idiomas oficiais em tempo real.

🧰 Bibliotecas Utilizadas
| Etapa | Bibliotecas | 
| Extração | requests, json | 
| Transformação | pandas, pyarrow | 
| Armazenamento | .parquet (formato colunar) | 
| Visualização | streamlit | 



Este projeto foi essencial para consolidar conceitos de arquitetura de dados, boas práticas de ETL e visualização interativa. Uma base sólida para projetos mais robustos em Data Engineering e Analytics!
