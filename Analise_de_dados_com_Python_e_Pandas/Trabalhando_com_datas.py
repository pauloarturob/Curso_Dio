import pandas as pd

# leitura dos arquivos
df1 = pd.read_excel("G:\Outros computadores\Meu computador\DOCUMENTOS\MEUS PROJETOS\Python\Curso Dio\Analise_de_dados_com_Python_e_Pandas\Arquivos\CFTV teste.xlsx")

# Transformando a colula em data em tipo inteiro
df1["CAM"] = df1["CAM"].astype("int64")

# Verificando o tipo de dado de cada coluna
df1.dtypes

# Transformando coluna de data em data
df1["CAM"] = pd.to_datetime(df1["Data"])

df1.dtypes

