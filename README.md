# 🛒 Projeto de Previsão de Vendas da rede de Farmácias Rossmann

Bem-vindo ao projeto de Previsão de Vendas Rossmann! Este repositório contém um pipeline completo de Ciência de Dados com o objetivo de prever as vendas diárias da rede de farmácias Rossmann.
A Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes das lojas Rossmann são responsáveis ​​por prever as vendas diárias com até seis semanas de antecedência. As vendas das lojas são influenciadas por diversos fatores, incluindo promoções, concorrência, feriados escolares e estaduais, sazonalidade e localização. Com milhares de gerentes fazendo previsões com base em suas circunstâncias específicas, a precisão dos resultados pode variar bastante.

## Desafio
Prever as vendas diárias de 1.115 lojas espalhadas pela Alemanha ao longo de um período de 6 semanas. Previsões de vendas confiáveis ​​permitem que os gerentes criem escalas de equipe eficientes, aumentando a produtividade e a motivação.

## 📌 Visão Geral do Projeto
O objetivo deste projeto é construir um modelo de Machine Learning robusto capaz de prever as vendas das lojas com base em dados históricos. Previsões de vendas precisas permitem uma melhor gestão de estoque, alocação de recursos e estratégia geral de negócios.

## 🛠️ Pipeline de Ciência de Dados
Este projeto segue um fluxo de trabalho estruturado de Ciência de Dados:
1.  **Descrição e Entendimento dos Dados**: Exploração inicial do conjunto de dados para entender suas dimensões, tipos de dados e valores ausentes.
2.  **Engenharia de Atributos (Feature Engineering)**: Criação de novas variáveis para capturar melhor os padrões subjacentes nos dados. Isso inclui:
    * Extração de variáveis baseadas em tempo (ano, mês, dia, semana do ano).
    * Cálculo do tempo desde a abertura dos concorrentes (`competition_time_month`).
    * Determinação da duração das promoções ativas (`promo_time_week`).
3.  **Análise Exploratória de Dados (EDA)**: Análise aprofundada de variáveis numéricas e categóricas para descobrir tendências e relações com a variável alvo (`sales`). Foram utilizadas visualizações como histogramas, gráficos de contagem (count plots) e boxplots.
4.  **Preparação dos Dados**: Formatação dos dados para modelagem, incluindo a codificação de variáveis categóricas e o dimensionamento (scaling) de variáveis numéricas.
5.  **Seleção de Atributos (Feature Selection)**: Identificação das características mais relevantes usando algoritmos como o Boruta para melhorar a eficiência e o desempenho do modelo.
6.  **Modelagem de Machine Learning**: Treinamento e avaliação do modelo XGBoost Regressor usando Validação Cruzada de Séries Temporais (Time Series Cross-Validation) para garantir previsões precisas em dados futuros.
7.  **Deploy (Em breve)**: Disponibilização do modelo via API (Flask/Render) e integração com um bot do Telegram para previsões em tempo real.

## 🚀 Principais Tecnologias Utilizadas
* Python 3.14.2
* Pandas, NumPy, Scikit-learn
* Seaborn, Matplotlib
* XGBoost Regressor, Random Forest Regressor, Linear Regression Lasso, Linear Regression
* Boruta

## 📈 Desempenho do Modelo
O XGBoost Regressor alcançou os seguintes resultados durante a validação cruzada:
* **MAE**: R$ 653.36
* **MAPE**: 9,5%
* **RMSE**: R$ 957.53