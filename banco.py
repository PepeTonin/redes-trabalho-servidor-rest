import mysql.connector
from mysql.connector import errorcode
from querys import *
import json


def receberDadosDoBanco():
    try:
        with open("cfg.json") as configFile:
            configFile_dict = json.load(configFile)
            # instancia um objeto mysql.connector na variavel db_connection
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password=configFile_dict["DbPass"],
                database=configFile_dict["DbName"],
            )

        cursor = db_connection.cursor()
        print("Conexão com o banco de dados feita!")

        resultado = dict()

        query = selectTable()
        cursor.execute(query)
        contents = cursor.fetchall()

        for i in range(len(contents)):
            resultado[i] = {
                "id": contents[i][0],
                "nome": contents[i][1],
                "telefone": contents[i][2],
            }

        cursor.close()
        print("Conexão com o banco encerrada!")

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


def enviarDadosAoBanco(dadosRecebidos: dict):
    try:
        # instancia um objeto mysql.connector na variavel db_connection
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pessoas*951*",
            database="trabalhoRedes",
        )

        cursor = db_connection.cursor()
        print("Conexão com o banco de dados feita!")

        query = insertIntoAgenda(
            dadosRecebidos.get("nome"), dadosRecebidos.get("telefone")
        )
        cursor.execute(query)
        db_connection.commit()
        print("Dados enviados ao banco!")

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
