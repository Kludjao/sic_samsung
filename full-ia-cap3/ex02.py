import pandas as pd
import os

# Vá para o diretório onde se encontra o arquivo de dados. 
os.chdir(r'C:\Users\Aluno\Desktop\projetosic\quiz\full-ia-cap3')  # Caminho do arquivo

# Ler o arquivo CSV
df = pd.read_csv('data_census.csv', header='infer')

# Exibir a forma do DataFrame e as 10 primeiras linhas
print("Shape do DataFrame:", df.shape)
print(df.head(10))

# 1) Qual é a população total onde a variável ProvinceCode seja igual a 115 ou 116?
populacao_total = df[df['ProvinceCode'].isin([115, 116])]['Population'].sum()
print("População total para ProvinceCode 115 ou 116:", populacao_total)

# 2) Qual é a população média das cidades onde há mais homens?
populacao_media = df[df['GenderRatio'] > 1]['Population'].mean()
print("População média das cidades com mais homens:", populacao_media)

# 3) Quais são os lugares com mais homens (GenderRatio > 1) e menos de 2 pessoas por domicílio (household)?
lugares_com_mais_homens = df[(df['GenderRatio'] > 1) & (df['Households'] < 2)]
print("Lugares com mais homens e menos de 2 pessoas por domicílio:")
print(lugares_com_mais_homens)

# 4) Ordenar o DataFrame por ordem ascendente dos domicílios (Households). Mostrar os 10 primeiros.
df_ordenado = df.sort_values(by='Households', ascending=True)
print("10 primeiros lugares ordenados por domicílios:")
print(df_ordenado.head(10))
