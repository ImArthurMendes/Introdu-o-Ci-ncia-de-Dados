# 1 - importanto bibliotecas
import pandas as pd
import numpy as np

# importanto dados
df_sales=pd.read_excel(
    'Dados_Sneakers_World3_Python.xlsx',
    sheet_name='Sales'
)

# 2 - exibição das dimensões originais no Data Frame
print('=' * 50)
print('Etapa 1 - Limpeza e transformação')
print('=' * 50)
print(f'\nDimensões originais: {df_sales.shape[0]} linhas x {df_sales.shape[1]} colunas')

# 3 - verificação dos tipos de dados
print('\n--- Tipos de dados ---')
print(df_sales.dtypes)

# 4 - verificação e remoção de linhas nulas
print('\n--- Valores nulos por coluna ---')
print(df_sales.isnull().sum())

# remoção de linhas que contenham ao menos um valor nulo
df_sales_limpo = df_sales.dropna()
print(f'\nDimensões após remoção de nulos: {df_sales.shape[0]} linhas x {df_sales.shape[1]} colunas')

# 5 - verificação e remoção de linhas duplicadas
print(f'\n--- Linhas duplicadas encontradas: {df_sales.duplicated().sum()} ---')

# remoção de linhas completamente duplicadas
df_sales=df_sales.drop_duplicates()
print(f'Dimensões após remoção de duplicatas: {df_sales.shape[0]} linhas x {df_sales.shape[1]} colunas')

# 6 - Resultado Final da limpeza e transformação
print('\n--- Primeiras linhas por Data Frame limpo ---')
print(df_sales.head())

print('\n Limpeza e transformação concluída com sucesso!')