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
    dbname="trabalho-banco",
    user="postgres",
    password="010801",
    host="localhost",
    port="5432"
)

############################################
#LER PLANILHA EXCEL E INSERIR DADOS NO BANCO
############################################

planilha = pd.read_excel("empresa1.xlsx")

for i, DADOS in enumerate(planilha['id']):
    dados1 = planilha.loc[i, "id"]
    dados2 = planilha.loc[i, "nome"]
    dados3 = planilha.loc[i, "cnpj"]

    dados = "INSERT INTO clienteempresa VALUES ('"+str(dados1)+"', '"+str(dados2)+"', '"+str(dados3)+"');"

    try:
        mycursor = connection.cursor()
        mycursor.execute(dados)
        connection.commit()
    except:
        continue

connection.close()
