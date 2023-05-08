def insertIntoAgenda(nome: str, telefone: str):
    query = f"""
        insert into agendaContatos (nome, telefone) values ("{nome}", "{telefone}");
    """
    return query


def insertIntoNomes(nome: str):
    query = f"""
        insert into nomes (nome) values ("{nome}");
    """
    return query


def insertIntoTelefones(idNome: int, telefone: str):
    query = f"""
        insert into telefones (idNome, telefone) values ({idNome}, "{telefone}");
    """
    return query


def insertIntoEnderecos(
    idNome: int, estado: str, cidade: str, bairro: str, rua: str, numero: int
):
    query = f"""
        insert into enderecos (idNome, estado, cidade, bairro, rua, numero)
        values ({idNome}, "{estado}", "{cidade}", "{bairro}", "{rua}", {numero});
    """
    return query


def insertIntoTable(dadosRecebidos: dict, tabelaReferencia: str):
    if tabelaReferencia == "nomes":
        nome = dadosRecebidos.get("nome")
        query = f"""
            insert into nomes (nome) values ("{nome}");
        """
        return query
    elif tabelaReferencia == "telefones":
        idNome = dadosRecebidos.get("idNome")
        telefone = dadosRecebidos.get("telefone")
        query = f"""
            insert into telefones (idNome, telefone) values ({idNome}, "{telefone}");
        """
        return query

    elif tabelaReferencia == "enderecos":
        idNome = dadosRecebidos.get("idNome")
        estado = dadosRecebidos.get("estado")
        cidade = dadosRecebidos.get("cidade")
        bairro = dadosRecebidos.get("bairro")
        rua = dadosRecebidos.get("rua")
        numero = dadosRecebidos.get("numero")
        query = f"""
            insert into enderecos (idNome, estado, cidade, bairro, rua, numero)
            values ({idNome}, "{estado}", "{cidade}", "{bairro}", "{rua}", {numero});
        """
        return query


def selectTable(tabelaReferencia: str):
    query = f"""
        select * from {tabelaReferencia};
    """
    return query
