import mysql.connector
from mysql.connector import errorcode
import json
from banco.querys import *


def adicionarElementoNaTabela(dadosRecebidos: dict, tabelaReferencia: str):
    try:
        # abre o arquivo "cfg.json" onde estão o nome da database e a senha
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
        # envia os dados ao banco
        query = insertIntoTable(dadosRecebidos, tabelaReferencia)
        cursor.execute(query)
        db_connection.commit()
        print("Dados enviados ao banco!")
        # encerra a conexão com o banco
        cursor.close()
        print("Conexão com o banco encerrada!")

    # em caso de algum erro, executa essa parte
    except mysql.connector.Error as error:
        # trata os diferentes erros
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Esse banco de dados não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos!")
        else:
            print(error)
