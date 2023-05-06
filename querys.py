def insertIntoAgenda(nome: str, telefone: str):
    query = f"""
        insert into agendaContatos (nome, telefone) values ("{nome}", "{telefone}");
    """
    return query


def selectTable():
    query = f"""
        select * from agendaContatos;
    """
    return query
