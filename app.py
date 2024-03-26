import os
import pandas as pd
from sqlalchemy import create_engine

# Lista para armazenar nomes de tabelas
nomes_tabelas = []

def carregar_dados(pasta_dados, engine):
    for arquivo in os.listdir(pasta_dados):
        extensao = arquivo.split('.')[-1].lower()
        if extensao in ['csv', 'xls', 'xlsx']:
            caminho_completo = os.path.join(pasta_dados, arquivo)

            if extensao == 'csv':
                df = pd.read_csv(caminho_completo)
            else:
                df = pd.read_excel(caminho_completo)

            nome_tabela = arquivo.split('.')[0]
            df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)

            nomes_tabelas.append(nome_tabela)

def consulta_sql(engine):
    while True:
        query = input("Digite sua consulta SQL ou 'exit' para sair: ")
        if query.lower() == 'exit':
            break
        try:
            resultado_df = pd.read_sql_query(query, con=engine)
            print(resultado_df.to_string(index=False))
        except Exception as e:
            print(f"Erro na consulta: {e}")

def main():
    pasta_dados = 'dados'
    engine = create_engine('sqlite://', echo=False)
    carregar_dados(pasta_dados, engine)
    print("Tabelas criadas:", ", ".join(nomes_tabelas))
    consulta_sql(engine)

if __name__ == "__main__":
    main()
