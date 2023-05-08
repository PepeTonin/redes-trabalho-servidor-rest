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
                "id": retornoBanco[i][0],
                "idNome": retornoBanco[i][1],
                "telefone": retornoBanco[i][2],
            }

    elif tabelaReferencia == "enderecos":
        for i in range(len(retornoBanco)):
            saida[i] = {
                "id": retornoBanco[i][0],
                "idNome": retornoBanco[i][1],
                "estado": retornoBanco[i][2],
                "cidade": retornoBanco[i][3],
                "bairro": retornoBanco[i][4],
                "rua": retornoBanco[i][5],
                "numero": retornoBanco[i][6],
            }

    return saida
