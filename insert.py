############################################
#                 IMPORTS
############################################
import psycopg as sql
import pandas as pd
import warnings
warnings.simplefilter("ignore")

############################################
#   CONEXÃO COM O BANCO DE DADOS POSTGRESQL
############################################

connection = sql.connect(
    dbname="nome-do-banco",
    user="postgres",
    password="senha",
    host="localhost",
    port="5432"
)

############################################
#LER PLANILHA EXCEL E INSERIR DADOS NO BANCO
############################################

planilha = pd.read_excel("arquivo.xlsx")

for i, DADOS in enumerate(planilha['coluna']):
    dados1 = planilha.loc[i, "coluna1"]
    dados2 = planilha.loc[i, "coluna2"]
    dados3 = planilha.loc[i, "coluna3"]

    dados = "INSERT INTO ClienteEmpresa VALUES ('"+str(dados1)+"', '"+str(dados2)+"', '"+str(dados3)+"');"

    try:
        mycursor = connection.cursor()
        mycursor.execute(dados)
        connection.commit()
    except:
        continue

connection.close()
