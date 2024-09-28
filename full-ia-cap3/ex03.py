import pandas as pd
import os

# Vá para o diretório onde se encontra o arquivo de dados.
os.chdir(r'C:\Users\Aluno\Desktop\projetosic\quiz\full-ia-cap3')  # Substitua pelo caminho correto

# Ler o arquivo CSV
df = pd.read_csv('data_sales.csv', header='infer')

# Exibir a forma do DataFrame e as primeiras 5 linhas
print("Shape do DataFrame:", df.shape)
print(df.head(5))

# 1) Anexe uma nova variável Amount = UnitPrice × Units
df['Amount'] = df['UnitPrice'] * df['Units']
print("DataFrame com nova coluna 'Amount':")
print(df.head(5))  # Verifique as primeiras linhas com a nova coluna

# 2) Calcule o preço unitário médio para cada região. Use o método groupby().
unit_price_mean_groupby = df.groupby('Region')['UnitPrice'].mean()
print("Preço unitário médio por região (groupby):")
print(unit_price_mean_groupby)

# 3) Calcule o preço unitário médio para cada região. Use o método pivot_table().
unit_price_mean_pivot = df.pivot_table(values='UnitPrice', index='Region', aggfunc='mean')
print("Preço unitário médio por região (pivot_table):")
print(unit_price_mean_pivot)

# 4) Calcule o preço unitário médio e as unidades para cada região em uma linha de código. Use o método groupby().
mean_price_units_groupby = df.groupby('Region').agg({'UnitPrice': 'mean', 'Units': 'sum'})
print("Preço unitário médio e total de unidades por região (groupby):")
print(mean_price_units_groupby)

# 5) Calcule o preço unitário médio e as unidades para cada região em uma linha de código. Use o método pivot_table().
mean_price_units_pivot = df.pivot_table(values=['UnitPrice', 'Units'], index='Region', aggfunc={'UnitPrice': 'mean', 'Units': 'sum'})
print("Preço unitário médio e total de unidades por região (pivot_table):")
print(mean_price_units_pivot)

# 6) Calcule o total de unidades para cada região e tipo de item em uma linha de código. Use o método pivot_table(). Preencha os valores faltantes com 0.
units_total_region_item = df.pivot_table(values='Units', index='Region', columns='Item', aggfunc='sum', fill_value=0)
print("Total de unidades por região e tipo de item (pivot_table):")
print(units_total_region_item)

# 7) Calcule o valor total de vendas para cada região e tipo de item em uma linha de código. Use o método pivot_table(). Preencha os valores faltantes com 0.
sales_total_region_item = df.pivot_table(values='Amount', index='Region', columns='Item', aggfunc='sum', fill_value=0)
print("Valor total de vendas por região e tipo de item (pivot_table):")
print(sales_total_region_item)
