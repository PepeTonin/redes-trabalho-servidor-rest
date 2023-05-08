import mysql.connector
from mysql.connector import errorcode
import json
from banco.querys import *
from banco.auxiliarBanco import *


def retornaTabela(tabelaReferencia: str):
    try:
        with open("./banco/cfg.json") as configFile:
            configFile_dict = json.load(configFile)
            # instancia um objeto mysql.connector na variavel db_connection
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password=configFile_dict["DbPass"],
                database=configFile_dict["DbName"],
            )
        # conecta ao banco
        cursor = db_connection.cursor()
        print("Conexão com o banco de dados feita!")
        # pega os dados de uma tabela do banco
        query = selectTable(tabelaReferencia)
        cursor.execute(query)
        contents = cursor.fetchall()
        # encerra a conexão com o banco
        cursor.close()
        print("Conexão com o banco encerrada!")
        # transforma o retorno do banco em dicionario
        resultado = dict()
        resultado = retornoBancoParaDict(tabelaReferencia, contents)
        # retorna o dicionário em formato json
        return json.dumps(resultado, indent=4)

    # em caso de algum erro, executa essa parte
    except mysql.connector.Error as error:
        # trata os diferentes erros
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Esse banco de dados não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos!")
        else:
            print(error)