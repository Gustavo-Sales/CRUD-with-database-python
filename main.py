import os

from database import criar_banco_dados
from pessoa_services import *
from conta_services import *


# ---- Ler e Imprimir as consultas salvas nas pastas

# Função para ler e imprimir arquivos em uma pasta
def ler_e_imprimir_arquivos_na_pasta(pasta):
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".txt"):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            with open(caminho_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}\n")



# ---------- Função principal para execução das funcionalidades -----------
 
def main():
    criar_banco_dados()
    inserir_dados_pessoa("nomes.txt")
    inserir_dados_conta("contas.txt")

    criar_pessoa() # colocar nos parenteses os dados da pessoa
    excluir_pessoa() # colocar o id da pessoa para excluir
    atualizar_pessoa() # colocar o id da pessoa e os novos dados

    criar_conta() # colocar nos parenteses os dados da conta
    excluir_conta() # colocar o id da conta para excluir
    atualizar_conta() # colocar o id da conta e os novos dados

    consultar_e_salvar_resultados_pessoa() # colocar o tipo de consulta (ex: primeiro_nome) e o que deseja pesquisar
    consultar_e_salvar_resultados_conta() # colocar o tipo de consulta (ex: agencia) e o que deseja pesquisar

    ler_e_imprimir_arquivos_na_pasta() # Colocar o nome da pasta (ex: "consulta_por_nome/resultados_nomes.txt")


if __name__ == "__main__":
    main()
    