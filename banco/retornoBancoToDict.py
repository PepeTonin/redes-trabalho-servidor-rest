# função auxiliar para transformar o retorno do banco, que é uma lista, em um dicionário
# varia de acordo com a tabela de origem
def retornoBancoParaDict(tabelaReferencia: str, retornoBanco: list):
    saida = dict()

    if tabelaReferencia == "nomes":
        for i in range(len(retornoBanco)):
            saida[i] = {
                "id": retornoBanco[i][0],
                "nome": retornoBanco[i][1],
            }

    elif tabelaReferencia == "telefones":
        for i in range(len(retornoBanco)):
            saida[i] = {
                "telefone": retornoBanco[i][0],
            }

    elif tabelaReferencia == "enderecos":
        for i in range(len(retornoBanco)):
            saida[i] = {
                "estado": retornoBanco[i][0],
                "cidade": retornoBanco[i][1],
                "bairro": retornoBanco[i][2],
                "rua": retornoBanco[i][3],
                "numero": retornoBanco[i][4],
            }

    elif tabelaReferencia == "todos_cadastros":
        for i in range(len(retornoBanco)):
            saida[i] = {
                "nome": retornoBanco[i][0],
                "telefone": retornoBanco[i][1],
                "estado": retornoBanco[i][2],
                "cidade": retornoBanco[i][3],
                "bairro": retornoBanco[i][4],
                "rua": retornoBanco[i][5],
                "numero": retornoBanco[i][6],
            }

    return saida
