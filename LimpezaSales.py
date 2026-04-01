# importanto bibliotecas
import pandas as pd
import numpy as np

# importanto dados
df_sales=pd.read_excel(
    'Dados_Sneakers_World3_Python.xlsx',
    sheet_name='Sales'
)

# exibição das dimensões originais no Data Frame
print('=' * 60)
print('Etapa 1 - Visão geral dos dados originais')
print('=' * 60)
print(f'\nDimensões originais: {df_sales.shape[0]} linhas x {df_sales.shape[1]} colunas')
print('\nPrimeiras linhas do Data Frame:')
print(df_sales.head())