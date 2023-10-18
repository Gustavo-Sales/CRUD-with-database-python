import sqlite3


db_url = "banco_dados.db"
conn = sqlite3.connect(db_url)

cursor = conn.cursor()

# Função para criar um banco de dados SQLite com as tabelas Pessoa e Conta
def criar_banco_dados():

    # Tabela Pessoa
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       cpf TEXT NOT NULL,
                       primeiro_nome TEXT NOT NULL,
                       nome_do_meio TEXT,
                       sobrenome TEXT NOT NULL,
                       idade INTEGER,
                       conta INTEGER,
                       FOREIGN KEY (conta) REFERENCES Conta(id))''')

    # Tabela Conta
    cursor.execute('''CREATE TABLE IF NOT EXISTS Conta
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       agencia TEXT NOT NULL,
                       numero TEXT NOT NULL,
                       saldo REAL,
                       gerente INTEGER,
                       titular INTEGER,
                       FOREIGN KEY (gerente) REFERENCES Pessoa(id),
                       FOREIGN KEY (titular) REFERENCES Pessoa(id))''')

    conn.commit()
    conn.close()
    