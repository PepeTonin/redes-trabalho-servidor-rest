# diferentes querys para inserir dados no banco
# varia de acordo com a tabela que se deseja inserir
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


# query para selecionar todos os dados de uma tabela
def selectTable(tabelaReferencia: str):
    query = f"""
        select * from {tabelaReferencia};
    """
    return query


# query para selecionar tabelas unidas de maneira adequada, filtrando apenas o idNome desejado
def selectJoinTablesItemId(tabelaReferencia: str, itemId: int):
    if tabelaReferencia == "telefones":
        query = f"""
            select telefones.telefone
            from nomes
            inner join telefones on nomes.id = telefones.idNome
            where nomes.id = {itemId};
        """
    elif tabelaReferencia == "enderecos":
        query = f"""
            select enderecos.estado, enderecos.cidade, enderecos.bairro, enderecos.rua, enderecos.numero
            from nomes
            inner join enderecos on nomes.id = enderecos.idNome
            where nomes.id = {itemId};
        """
    return query


# query para selecionar tabelas unidas de maneira adequada, sem filtros, traz todos os dados mesmo
def selectJoinTablesAll():
    query = f"""
        select nomes.nome, telefones.telefone, enderecos.estado, enderecos.cidade, enderecos.bairro, enderecos.rua, enderecos.numero
        from nomes
        inner join telefones on nomes.id = telefones.idNome
        inner join enderecos on nomes.id = enderecos.idNome;
    """
    return query
