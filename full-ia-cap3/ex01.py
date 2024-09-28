import pandas as pd
import os


os.chdir(r'C:\Users\Aluno\Desktop\projetosic\quiz\full-ia-cap3')  
# Ler o arquivo CSV
df = pd.read_csv('data_studentlist.csv', header='infer')

# 1) Qual é a altura média dos estudantes do sexo masculino?
altura_media_masculino = df[df['sexo'] == 'M']['altura'].mean()

# 2) Qual é a altura média das estudantes do sexo feminino?
altura_media_feminino = df[df['sexo'] == 'F']['altura'].mean()

# 3) Qual é o peso médio dos estudantes do sexo masculino?
peso_medio_masculino = df[df['sexo'] == 'M']['peso'].mean()

# 4) Qual é o peso médio das estudantes do sexo feminino?
peso_medio_feminino = df[df['sexo'] == 'F']['peso'].mean()

# 5) Qual é a altura do estudante mais alto do sexo masculino?
altura_maxima_masculino = df[df['sexo'] == 'M']['altura'].max()

# 6) Qual é a altura da estudante mais baixa do sexo feminino?
altura_minima_feminino = df[df['sexo'] == 'F']['altura'].min()

# 7) Qual é o menor peso entre os estudantes de sexo masculino de altura superior a 175cm?
menor_peso_masculino_acima_175 = df[(df['sexo'] == 'M') & (df['altura'] > 175)]['peso'].min()

# 8) Qual é o maior peso entre as estudantes de sexo feminino de altura inferior a 160cm?
maior_peso_feminino_abaixo_160 = df[(df['sexo'] == 'F') & (df['altura'] < 160)]['peso'].max()

# 9) Qual é a nota média dos estudantes sem ausência ('N')?
nota_media_sem_ausencia = df[df['ausencia'] == 'N']['nota'].mean()

# 10) Qual é a nota média dos estudantes com ausência ('Y')?
nota_media_com_ausencia = df[df['ausencia'] == 'Y']['nota'].mean()

# 11) Qual é a altura média dos alunos com tipo sanguíneo 'A' ou 'AB'?
altura_media_tipo_sanguineo = df[df['tipo_sanguineo'].isin(['A', 'AB'])]['altura'].mean()

# 12) Qual é a altura média dos estudantes do sexo masculino com tipo sanguíneo 'A' ou 'AB'?
altura_media_masculino_tipo_sanguineo = df[(df['sexo'] == 'M') & (df['tipo_sanguineo'].isin(['A', 'AB']))]['altura'].mean()

# 13) Qual é a idade média dos estudantes com ausência ('Y') cuja nota é igual ou maior que 3?
idade_media_com_ausencia_nota_maior_3 = df[(df['ausencia'] == 'Y') & (df['nota'] >= 3)]['idade'].mean()

# Exibindo os resultados
print("Altura média dos estudantes do sexo masculino:", altura_media_masculino)
print("Altura média das estudantes do sexo feminino:", altura_media_feminino)
print("Peso médio dos estudantes do sexo masculino:", peso_medio_masculino)
print("Peso médio das estudantes do sexo feminino:", peso_medio_feminino)
print("Altura do estudante mais alto do sexo masculino:", altura_maxima_masculino)
print("Altura da estudante mais baixa do sexo feminino:", altura_minima_feminino)
print("Menor peso entre os estudantes de sexo masculino de altura superior a 175cm:", menor_peso_masculino_acima_175)
print("Maior peso entre as estudantes de sexo feminino de altura inferior a 160cm:", maior_peso_feminino_abaixo_160)
print("Nota média dos estudantes sem ausência ('N'):", nota_media_sem_ausencia)
print("Nota média dos estudantes com ausência ('Y'):", nota_media_com_ausencia)
print("Altura média dos alunos com tipo sanguíneo 'A' ou 'AB':", altura_media_tipo_sanguineo)
print("Altura média dos estudantes do sexo masculino com tipo sanguíneo 'A' ou 'AB':", altura_media_masculino_tipo_sanguineo)
print("Idade média dos estudantes com ausência ('Y') cuja nota é igual ou maior que 3:", idade_media_com_ausencia_nota_maior_3)
