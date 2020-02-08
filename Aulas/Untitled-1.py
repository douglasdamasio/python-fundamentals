#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Aulas'))
	print(os.getcwd())
except:
	pass
#%%
import pandas as pd # Importa a biblioteca


#%%
get_ipython().system('pwd')


#%%
df = pd.read_csv('dados/campeonato-brasileiro-full.csv') # Importa o arquivo pra dentro da IDE


#%%
df


#%%
df.shape


#%%
df


#%%
df2 = df


#%%
df2


#%%
df2.drop([0,15]) #Remover linhas pelo index


#%%
df2.drop('Horário', axis=1) #Remove coluna


#%%
df2.index # Retornar o Range


#%%
df2.count() # Conta vazio


#%%
df2['Quantidade de gols'] = df2['Clube 1 Gols'] + df2['Clube 2 Gols']


#%%
df2


#%%
df2.to_csv('novo_arquivo.csv')


#%%
df['Quantidade de gols'].max()


#%%
df.columns


#%%
df.apply(lambda x: x.replace('Palmeiras', 'Palmeiras-SP'))


#%%
df.drop('Resultado', axis=1)


#%%



