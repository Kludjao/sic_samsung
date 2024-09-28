import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Vá para o diretório onde se encontra o arquivo de dados.
os.chdir(r'C:\Users\Aluno\Desktop\projetosic\quiz\full-ia-cap3')  # Substitua pelo caminho correto

# Ler o arquivo CSV
df = pd.read_csv('data_coffeeshop.csv', header='infer', na_values=[' '])

# Exibir a forma do DataFrame e as primeiras 5 linhas
print("Shape do DataFrame:", df.shape)
print(df.head(5))

# 1) Tabela de frequência de 'yearOfStart' e visualização por ano
year_frequency = df['yearOfStart'].value_counts().sort_index()
print("Tabela de frequência por ano:")
print(year_frequency)

# Gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(year_frequency.index, year_frequency.values, marker='o')
plt.title('Frequência de Abertura de Cafeterias por Ano (1997-2014)')
plt.xlabel('Ano')
plt.ylabel('Frequência')
plt.xticks(year_frequency.index, rotation=45)
plt.xlim(1997, 2014)
plt.grid()
plt.show()

# 2) Dividir os dados pelo estado atual dos negócios ("In" ou "Out") e visualizar a tendência
df_in = df[df['status'] == 'In']
df_out = df[df['status'] == 'Out']

# Frequências por ano para "In" e "Out"
year_frequency_in = df_in['yearOfStart'].value_counts().sort_index()
year_frequency_out = df_out['yearOfStart'].value_counts().sort_index()

# Gráfico com duas linhas
plt.figure(figsize=(10, 5))
plt.plot(year_frequency_in.index, year_frequency_in.values, marker='o', label='In')
plt.plot(year_frequency_out.index, year_frequency_out.values, marker='o', label='Out')
plt.title('Tendência Anual de Abertura de Cafeterias (1997-2014)')
plt.xlabel('Ano')
plt.ylabel('Frequência')
plt.xticks(year_frequency_in.index, rotation=45)
plt.xlim(1997, 2014)
plt.legend()
plt.grid()
plt.show()

# 3) Análise da tendência
print("""
Análise da Tendência:
- A partir do gráfico da frequência anual, é possível observar que a abertura de cafeterias teve um aumento notável nos anos entre 1997 e 2014.
- Ao analisar as linhas 'In' e 'Out', é possível notar que, em geral, a tendência de abertura ('In') é maior que a de fechamento ('Out'), indicando um crescimento no setor de cafeterias ao longo dos anos.
- A partir de 2010, há uma diminuição no número de aberturas, que pode indicar uma saturação do mercado ou mudanças nas preferências dos consumidores.
""")
