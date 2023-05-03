import mysql.connector
from mysql.connector import errorcode

try:
    # instancia um objeto mysql.connector na variavel db_connection
    db_connection = mysql.connector.connect(
    host='localhost', user='root', password='Pessoas*951*', database='aulaIntegracaoSQLePY')
    print('Conexão com o banco de dados feita!')
    # em caso de algum erro, executa essa parte
except mysql.connector.Error as error:
    # trata os diferentes erros
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print('Esse banco de dados não existe!')
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuário ou senha inválidos!')
    else:
        print(error)
cursor = db_connection.cursor()
