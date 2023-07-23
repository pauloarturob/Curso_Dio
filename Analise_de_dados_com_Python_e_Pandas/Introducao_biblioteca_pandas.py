import pandas as pd

df = pd.read_csv("G:\Outros computadores\Meu computador\DOCUMENTOS\MEUS PROJETOS\Python\Curso Dio\Analise_de_dados_com_Python_e_Pandas\Arquivos\CFTV.csv",error_bad_lines=False, sep=";")
print(df)

#Retorna as 5 primeiras linhas

R = df.head()
print(R)

T = df.columns
print(T)

Y = df.dtypes
print(Y)

U = df.tail(1)
print(U)

I = df.describe()
print(I)

P = df["LUGAR"].unique()
print(P)

