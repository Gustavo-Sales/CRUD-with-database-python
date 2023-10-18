import os

from database import cursor, conn


# Função para ler dados de um arquivo de texto e inserir no banco de dados
def inserir_dados_pessoa(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas[1:]:  # Ignorar a primeira linha com cabeçalho
            partes = linha.strip().split(" ")
            cpf, primeiro_nome, nome_do_meio, sobrenome, idade, conta = partes
            cursor.execute("INSERT INTO Pessoa (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, conta) VALUES (?, ?, ?, ?, ?, ?)",
                           (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, conta))

    conn.commit()
    conn.close()


# ---- CRUD Pessoa ------

# Função para criar uma nova pessoa
def criar_pessoa(cpf, primeiro_nome, nome_do_meio, sobrenome, idade):
    cursor.execute("INSERT INTO Pessoa (cpf, primeiro_nome, nome_do_meio, sobrenome, idade) VALUES (?, ?, ?, ?, ?)",
                   (cpf, primeiro_nome, nome_do_meio, sobrenome, idade))
    conn.commit()
    conn.close()


# Função para excluir uma pessoa pelo ID
def excluir_pessoa(id):
    cursor.execute("DELETE FROM Pessoa WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Função para atualizar informações de uma pessoa
def atualizar_pessoa(id, cpf, primeiro_nome, nome_do_meio, sobrenome, idade):
    cursor.execute("UPDATE Pessoa SET cpf=?, primeiro_nome=?, nome_do_meio=?, sobrenome=?, idade=? WHERE id=?",
                   (cpf, primeiro_nome, nome_do_meio, sobrenome, idade, id))
    conn.commit()
    conn.close()


# ---- Consultar e guardar resultados em pastas e arquivos txt

# Função para realizar consultas e salvar os resultados em arquivos TXT
def consultar_e_salvar_resultados_pessoa(tipo_consulta, pesquisa):

    # Certificar-se de que as pastas existem ou criá-las
    pasta = f"consulta_por_{tipo_consulta}"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Consulta no banco de dados
    cursor.execute(f"SELECT * FROM Pessoa WHERE {tipo_consulta}=?", ({pesquisa},))
    resultados = cursor.fetchall()
    salvar_resultados(resultados, f"consulta_por_{tipo_consulta}/resultado_{pesquisa}.txt")

    # Fechar a conexão com o banco de dados
    conn.close()


# Função para salvar resultados em um arquivo TXT
def salvar_resultados(resultados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for resultado in resultados:
            arquivo.write(f"{resultado}\n")
            