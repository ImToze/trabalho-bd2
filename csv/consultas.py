import time  # Para medir o tempo de execução
import csv  # Para criar o arquivo CSV
import psycopg as sql
import pandas as pd
import warnings
warnings.simplefilter("ignore")

conexao = sql.connect(
    dbname="trabalho-banco",
    user="postgres",
    password="010801",
    host="localhost",
    port="5432"
)

resultados = []

for i in range(1, 101):
    
    tempo_inicio = time.time()

    
    consulta = "SELECT DISTINCT T.MARCA, COUNT(T.MARCA) AS QUANTIDADE FROM TAXI T JOIN MOTORISTA M ON M.PLACA = T.PLACA GROUP BY T.MARCA"
    with conexao.cursor() as cursor:
        cursor.execute(consulta)
        dados = cursor.fetchall()  

    
    tempo_execucao = time.time() - tempo_inicio

    resultados.append((i, tempo_execucao))

df = pd.DataFrame(resultados, columns=["Posição", "Tempo"])

nome_arquivo = "tempos_execucao.csv"
df.to_csv(nome_arquivo, index=False)

print(f"Resultados salvos em {nome_arquivo}")

conexao.close()