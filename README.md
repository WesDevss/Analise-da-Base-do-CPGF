# 📊 Análise e Visualização de Gastos Financeiros 💰

Este projeto realiza uma análise de dados financeiros de um arquivo CSV, com foco em gastos por órgão, categorias e a evolução dos gastos ao longo do tempo. A seguir, é descrito o processo que o código executa e como utilizar este projeto para suas próprias análises.

## Funcionalidades 🚀

1. **Leitura do Arquivo CSV** 📑: O arquivo é carregado utilizando a biblioteca `pandas` e processado para garantir que todos os dados estejam corretos.
2. **Preparação e Limpeza de Dados** 🧹:
   - Valores nulos são removidos.
   - A coluna de **Data de Transação** é convertida para o formato de data.
   - A coluna de **Valor de Transação** é convertida para tipo numérico.
3. **Análise** 📈:
   - **Total de Gastos**: O código calcula o total gasto com base na coluna **Valor de Transação**.
   - **Média de Gastos por Órgão**: Caso a coluna **Órgão Superior** esteja presente, a média dos gastos por órgão é calculada.
4. **Visualização** 🎨:
   - **Gráfico de Gastos por Órgão**: Um gráfico de barras é gerado para os 10 órgãos com maiores gastos médios.
   - **Evolução dos Gastos ao Longo do Tempo**: Um gráfico de linha mostra a evolução dos gastos ao longo dos meses.
   
   Ambos os gráficos são salvos como imagens PNG para facilitar o compartilhamento ou a análise posterior.

## Como Utilizar 🛠️

1. **Pré-requisitos**:
   - Python 3.x 🐍
   - Bibliotecas:
     - `pandas` 📊
     - `matplotlib` 📉
     - `seaborn` 🎨
   
   Caso ainda não tenha essas bibliotecas instaladas, você pode instalá-las utilizando o seguinte comando:
   ```bash
   pip install pandas matplotlib seaborn
