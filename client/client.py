import streamlit as st
from client_requests import *

URL = "http://127.0.0.1:8000"

tab1, tab2, tab3 = st.tabs(
    [
        "Adicionar novo cadastro",
        "Adicionar dados a cadastro existente",
        "Consultar cadastros",
    ]
)


with tab1:
    st.header("Adicionar novo cadastro")
    with st.form("form_adicionar_novo"):
        nome = st.text_input("nome")
        telefone = st.text_input("telefone")
        st.write("endereco")
        estado = st.text_input("estado")
        cidade = st.text_input("cidade")
        bairro = st.text_input("bairro")
        rua = st.text_input("rua")
        numero = st.number_input("numero", min_value=0)

        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            # faz um post para a tabela de nomes
            postNomes(nome)
            # faz um get na tabela de nomes para buscar os ids
            conteudo = getNomes()
            # encontra o id do nome adicionado
            for elemento in conteudo.values():
                if elemento["nome"] == nome:
                    idNome = elemento["id"]
            # usa esse id para adicionar os outros dados
            # faz um post para a tabela de telefones
            postTelefones(idNome, telefone)
            # faz um post para a tabela de enderecos
            postEnderecos(idNome, estado, cidade, bairro, rua, numero)


with tab2:
    st.header("Adicionar dados a cadastro existente")
    tab2_1, tab2_2 = st.tabs(["Telefone", "Endereco"])
    with tab2_1:
        st.header("Adicionar telefone a cadastro existente")
        # faz um metodo get na tabela de nomes para obter listas
        # com os nomes e seus repectivos ids já cadastrados
        conteudo = getNomes()
        listaIds = list()
        listaNomes = list()
        for elemento in conteudo.values():
            listaIds.append(elemento["id"])
            listaNomes.append(elemento["nome"])

        with st.form("form_novo_telefone"):
            nome = st.selectbox(
                "Nome", listaNomes, key="nome para adicionar novo telefone"
            )
            telefone = st.text_input("telefone")

            submitted = st.form_submit_button("Cadastrar")

            if submitted:
                # pega o valor que está na lista de ids, na mesma posição que
                # o nome selecionado na lista de nomes
                idNome = listaIds[listaNomes.index(nome)]
                # faz um post para a tabela de telefones
                postTelefones(idNome, telefone)

    with tab2_2:
        st.header("Adicionar endereco a cadastro existente")
        # faz um metodo get na tabela de nomes para obter listas
        # com os nomes e seus repectivos ids já cadastrados
        conteudo = getNomes()
        listaIds = list()
        listaNomes = list()
        for elemento in conteudo.values():
            listaIds.append(elemento["id"])
            listaNomes.append(elemento["nome"])

        with st.form("form_novo_endereco"):
            nome = st.selectbox(
                "Nome", listaNomes, key="nome para adicionar novo endereco"
            )
            estado = st.text_input("estado")
            cidade = st.text_input("cidade")
            bairro = st.text_input("bairro")
            rua = st.text_input("rua")
            numero = st.number_input("numero", min_value=0)

            submitted = st.form_submit_button("Cadastrar")

            if submitted:
                # pega o valor que está na lista de ids, na mesma posição que
                # o nome selecionado na lista de nomes
                idNome = listaIds[listaNomes.index(nome)]
                # faz um post para a tabela de telefones
                postEnderecos(idNome, estado, cidade, bairro, rua, numero)

with tab3:
    st.header("Consultar cadastros")
    tab3_1, tab3_2 = st.tabs(["Consultar por nome", "Ver todos os cadastros"])
    with tab3_1:
        # faz um metodo get na tabela de nomes para obter listas
        # com os nomes e seus repectivos ids já cadastrados
        conteudo = getNomes()
        listaIds = list()
        listaNomes = list()
        for elemento in conteudo.values():
            listaIds.append(elemento["id"])
            listaNomes.append(elemento["nome"])

        with st.form("form_pesquisar_por_nome"):
            nome = st.selectbox(
                "Nome", listaNomes, key="nome para pesquisar na lista de cadastro"
            )

            submitted = st.form_submit_button("Pesquisar")

            if submitted:
                # pega o valor que está na lista de ids, na mesma posição que
                # o nome selecionado na lista de nomes
                idNome = listaIds[listaNomes.index(nome)]
                resultado = getCadastrosPorNome(idNome)
                st.write(f"Mostrando resultados para **{nome}**")
                st.table(resultado)
    with tab3_2:
        st.write("**Mostrando todos os cadastros**")
        st.table(getTodosOsCadastros())
