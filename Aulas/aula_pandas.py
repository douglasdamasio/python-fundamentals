# ######### pandas ###########

# Importação do pandas
import pandas as pandas

# Importa o arquivo pra dentro da IDE
df = pd.read_csv('dados/campeonato-brasileiro-full.csv')

# Mostra a quantidade de linhas e colunas
df.shape

# Mostrar conteudo do começo do dataset 
# Default is 5 rows
df.head(20)

# Nunca manipular o dataset original
df2 = df

# Remover linhas pelo index
df2.drop([0, 15])

# Remover coluna (axis funciona como um True)
df2.drop('Horário', axis=1)

# Retornar o Range
df2.index

# Conta vazio
df2.count()

# Inserção de uma nova coluna de dados
df2['Quantidade de gols'] = df2['Clube 1 Gols'] + df2['Clube 2 Gols']

# Grava o dataset em um novo arquivo (DE UMA FORMA MUITO ESTRANHA)
df2.to_csv('novo_arquivo.csv')

# Exibir o valor maximo de uma coluna
df2['Quantidade de gols'].max()

# Exibe o Index do dataset
df2.columns

# Função anonima dentro do dataset
df2.apply(lambda x: x.replace('Palmeiras', 'Palmeiras-SP'))
