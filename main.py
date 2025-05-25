from biblioteca import Biblioteca, Livro
import utils
import random
import json


biblioteca = Biblioteca("Alex Library")


def main():
    print("\nGerenciador de Biblioteca\n")
    while True:
        print(f"\n{biblioteca.nome}\n")
        print("Escolha oque deseja fazer")
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

        if opcao == "1":
            livroTitulo = input("Digite o título do livro: ")
            livroAutor = input("Digite o autor do livro: ")
            livroAnoDePublicacao = input("Digite o ano de publicação do livro: ")

            if utils.verificar_ano_de_publicacao(livroAnoDePublicacao) == False:
                print("Digite um ano de publicaçao valido")

            else:
                data = utils.ler_dados()
                randomID = str(random.randint(1000, 9999))

                for livro in data["lista_livros"]:
                    if livro["id"] == randomID:
                        randomID = str(random.randint(1000, 9999))

                NovoLivro = Livro(
                    livroTitulo,
                    livroAutor,
                    livroAnoDePublicacao,
                    randomID,
                    "Disponivel",
                )
                print(biblioteca.adicionar_livro(NovoLivro))

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            livro_ID = input("Digite o ID do livro que deseja editar: ")
            livro_novo_titulo = input("Digite o novo título do livro: ")
            livro_novo_autor = input("Digite o novo autor do livro: ")
            livro_novo_ano_de_publicacao = input(
                "Digite o novo ano de publicação do livro: "
            )

            if utils.verificar_ano_de_publicacao(livro_novo_ano_de_publicacao) == False:
                print("Digite um ano de publicaçao valido")

            elif utils.verificar_id(livro_ID) == False:
                print("Digite um ID valido")

            else:

                try:
                    print(
                        biblioteca.editar_livro(
                            livro_novo_titulo,
                            livro_novo_autor,
                            livro_novo_ano_de_publicacao,
                            livro_ID,
                        )
                    )

                except:
                    print("Ocorreu um erro ao tentar editar o livro")

        elif opcao == "4":
            livroID = input("Digite o ID do livro que deseja excluir: ")

            if utils.verificar_id(livroID) == False:
                print("Digite um numero de ID valido")

            else:
                try:
                    print(biblioteca.remover_livro(livroID))

                except:
                    print("Ocorreu um erro ao tentar excluir o livro")

        elif opcao == "5":
            livroTitulo = input("Digite o título do livro que deseja buscar: ")
            print("")

            try:
                print("Livros encontrados:")
                livro_encontrado = biblioteca.buscar_livro(livroTitulo)
                if livro_encontrado == False:
                    print("Nenhum livro encontrado")

            except:
                print(
                    "Ocorreu um erro ao tentar buscar o livro, verefique o titulo ou se o livro existe"
                )
        elif opcao == "6":
            biblioteca.gerar_relatorio()

        elif opcao == "7":
            livroID = input("Digite o ID do livro que deseja mudar o status: ")
            if utils.verificar_id(livroID) == False:
                print("Digite um numero de ID valido")

            else:
                print(biblioteca.gerenciar_status(livroID))

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
