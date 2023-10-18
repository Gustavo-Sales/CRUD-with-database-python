import os

from database import cursor, conn


# Função para ler dados de um arquivo de texto e inserir na tabela Conta
def inserir_dados_conta(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas[1:]:  # Ignorar a primeira linha com cabeçalho
            partes = linha.strip().split(" ")
            agencia, numero, saldo, gerente, titular = partes
            cursor.execute("INSERT INTO Conta (agencia, numero, saldo, gerente, titular) VALUES (?, ?, ?, ?, ?)",
                           (agencia, numero, saldo, gerente, titular))

    conn.commit()
    conn.close()


# ------ CRUD Conta ---------

# Função para criar uma nova conta
def criar_conta(agencia, numero, saldo, gerente, titular):
    cursor.execute("INSERT INTO Conta (agencia, numero, saldo, gerente, titular) VALUES (?, ?, ?, ?, ?)",
                   (agencia, numero, saldo, gerente, titular))
    conn.commit()
    conn.close()


# Função para excluir uma conta pelo ID
def excluir_conta(id):
    cursor.execute("DELETE FROM Conta WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Função para atualizar informações de uma conta
def atualizar_conta(id, agencia, numero, saldo, gerente, titular):
    cursor.execute("UPDATE Conta SET agencia=?, numero=?, saldo=?, gerente=?, titular=? WHERE id=?",
                   (agencia, numero, saldo, gerente, titular, id))
    conn.commit()
    conn.close()


# Função para realizar consultas e salvar os resultados em arquivos TXT
def consultar_e_salvar_resultados_conta(tipo_consulta, pesquisa):
    
    # Certificar-se de que as pastas existem ou criá-las
    pasta = f"consulta_por_{tipo_consulta}"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Consulta no banco de dados
    cursor.execute(f"SELECT * FROM Conta WHERE {tipo_consulta}=?", ({pesquisa},))
    resultados = cursor.fetchall()
    salvar_resultados(resultados, f"consulta_por_{tipo_consulta}/resultado_{pesquisa}.txt")

    # Fechar a conexão com o banco de dados
    conn.close()


# Função para salvar resultados em um arquivo TXT
def salvar_resultados(resultados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for resultado in resultados:
            arquivo.write(f"{resultado}\n")
            