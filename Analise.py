import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Configura o backend para imagens estáticas

# Tente abrir o arquivo especificando possíveis problemas
try:

    arquivo = "202401_CPGF.csv"  
    
    # Leitura inicial para detectar problemas (ajuste o separador e codificação conforme necessário)
    df = pd.read_csv(arquivo, sep=";", encoding="ISO-8859-1", on_bad_lines='skip')  # Substituindo error_bad_lines por on_bad_lines
    
    # Inspecionar as primeiras linhas
    print("Primeiras linhas do dataset corrigido:")
    print(df.head())
    
    # Passo 2: Limpeza e Preparação
    # Remover valores nulos
    df.dropna(inplace=True)

    # Converter a coluna 'DATA TRANSAÇÃO' para formato de data
    df['DATA TRANSAÇÃO'] = pd.to_datetime(df['DATA TRANSAÇÃO'], format='%d/%m/%Y')

    # Converter a coluna 'VALOR TRANSAÇÃO' para float
    df['VALOR TRANSAÇÃO'] = df['VALOR TRANSAÇÃO'].replace({',': '.'}, regex=True).astype(float)

    # Verificar as informações gerais
    print("\nInformações gerais:")
    print(df.info())

    # Passo 3: Análise básica
    # Total gasto
    total_gasto = df['VALOR TRANSAÇÃO'].sum()
    print(f"\nTotal gasto: R${total_gasto:,.2f}")

    # Média de gastos por órgão
    if 'NOME ÓRGÃO SUPERIOR' in df.columns:
        gastos_por_orgao = df.groupby('NOME ÓRGÃO SUPERIOR')['VALOR TRANSAÇÃO'].mean().sort_values(ascending=False)
        print("\nMédia de gastos por órgão:")
        print(gastos_por_orgao)
    else:
        print("\nColuna 'NOME ÓRGÃO SUPERIOR' não encontrada. Verifique o nome da coluna.")

    # Passo 4: Visualização
    # Gráfico 1: Gastos por Órgão (caso a coluna exista)
    if 'NOME ÓRGÃO SUPERIOR' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=gastos_por_orgao.index[:10], y=gastos_por_orgao.values[:10], palette='coolwarm')
        plt.title('Média de Gastos por Órgão (Top 10)')
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Órgão')
        plt.ylabel('Valor Médio (R$)')
        plt.savefig('grafico_gastos_por_orgao.png')  # Salvar o gráfico
        print("Gráfico de gastos por órgão salvo como 'grafico_gastos_por_orgao.png'.")

    # Gráfico 2: Evolução dos gastos ao longo do tempo
    if 'DATA TRANSAÇÃO' in df.columns:
        df['Mês'] = df['DATA TRANSAÇÃO'].dt.to_period('M')
        gastos_por_mes = df.groupby('Mês')['VALOR TRANSAÇÃO'].sum()

        plt.figure(figsize=(12, 6))
        plt.plot(gastos_por_mes.index.astype(str), gastos_por_mes.values, marker='o', linestyle='-', color='blue')
        plt.title('Evolução dos Gastos ao Longo do Tempo')
        plt.xlabel('Mês')
        plt.ylabel('Total Gasto (R$)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.savefig('grafico_evolucao_gastos.png')  # Salvar o gráfico
        print("Gráfico de evolução dos gastos salvo como 'grafico_evolucao_gastos.png'.")

except UnicodeDecodeError:
    print("Erro de decodificação! Tente mudar a codificação para UTF-8.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
