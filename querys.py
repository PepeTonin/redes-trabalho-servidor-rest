def insertIntoNomes(nome: str):
    query = f"""
        insert into nomes (nome) values ("{nome}")
    """
    return query


def insertIntoTelefones(telefone: str):
    query = f"""
        insert into telefones (telefone) values ("{telefone}")
    """
    return query
