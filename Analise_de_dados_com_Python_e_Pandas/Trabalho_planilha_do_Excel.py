import pandas as pd

# leitura dos arquivos
df1 = pd.read_excel("G:\Outros computadores\Meu computador\DOCUMENTOS\MEUS PROJETOS\Python\Curso Dio\Analise_de_dados_com_Python_e_Pandas\Arquivos\CFTV teste.xlsx")
df2 = pd.read_excel("G:\Outros computadores\Meu computador\DOCUMENTOS\MEUS PROJETOS\Python\Curso Dio\Analise_de_dados_com_Python_e_Pandas\Arquivos\CFTV teste 2.xlsx")

# print(df1.head())
# Juntando todos dados
df = pd.concat([df1,df2])
print(df)

# Exibindo as 5 primeiras linhas
A = df.head()
print(A)

# Exibindo as 5 umitmas linhas
B = df.tail()
print(B)

# Pegar uma amostra de dados, pega uma amostra aleatorias
C = df.sample(4)
print(C)

