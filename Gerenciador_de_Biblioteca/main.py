from biblioteca import Biblioteca
from opcoes import *

def main():
    print("\nGerenciador de Biblioteca")
    while True:
        print("\nEscolha oque deseja fazer")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Editar Livro")
        print("4. Excluir Livro")
        print("5. Buscar Livro")
        print("6. Gerar Relatório")
        print("7. Gerenciar Status")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")
        print("")

        opcoes = {
            "1": adicionar_livro,
            "2": listar_livros,
            "3": editar_livro,
            "4": excluir_livro,
            "5": buscar_livro,
            "6": gerar_relatorio,
            "7": gerenciar_status,
            "8": sair,
        }
        if opcao in opcoes:
            opcoes[opcao]()

        else:
            print("Opcao invalida, tente novamente")


if __name__ == "__main__":
    main()
