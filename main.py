from biblioteca import Biblioteca, Livro
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
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        print("")
        if opcao == "1":
            livroTitulo = input("Digite o título do livro: ")
            livroAutor = input("Digite o autor do livro: ")
            livroAnoDePublicacao = input("Digite o ano de publicação do livro: ")

            if livroAnoDePublicacao.isdigit() == False:
                print("Por favor digite um numero valido")

            with open("livros.json", "r") as f:
                data = json.loads(f.read())
                randomID = str(random.randint(1000, 9999))
                for livro in data["lista_livros"]:
                    if livro["id"] == randomID:
                        randomID = str(random.randint(1000, 9999))

            NovoLivro = Livro(
                livroTitulo, livroAutor, livroAnoDePublicacao, randomID, "Disponivel"
            )
            biblioteca.adicionar_livro(NovoLivro)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            livroID = input("Digite o ID do livro que deseja editar: ")
            livroNovoTitulo = input("Digite o novo título do livro: ")
            livroNovoAutor = input("Digite o novo autor do livro: ")
            livroNovoAnoDePublicacao = input(
                "Digite o novo ano de publicação do livro: "
            )

            if livroNovoAnoDePublicacao.isdigit() == False:
                print("Por favor digite um numero de publicaçao valido")

            elif livroID.isdigit() == False:
                print("Por favor digite um numero de ID valido")

            else:

                try:
                    resultado = biblioteca.editar_livro(
                        livroNovoTitulo,
                        livroNovoAutor,
                        livroNovoAnoDePublicacao,
                        livroID,
                    )
                    if resultado == True:
                        print("Livro editado com sucesso")
                    else:
                        print("Livro não encontrado")

                except:
                    print("Ocorreu um erro ao tentar editar o livro")

        elif opcao == "4":
            livroID = input("Digite o ID do livro que deseja excluir: ")
            if livroID.isdigit() == False:
                print("Por favor digite um numero de ID valido")

            else:
                try:
                    resultado = biblioteca.remover_livro(livroID)
                    if resultado == True:
                        print("Livro excluido com sucesso")
                    else:
                        print("Livro não encontrado")
                except:
                    print("Ocorreu um erro ao tentar excluir o livro")

        elif opcao == "5":
            livroTitulo = input("Digite o título do livro que deseja buscar: ")
            print("")

            try:
                print("Livros encontrados:")
                resultado = biblioteca.buscar_livro(livroTitulo)
                if resultado == False:
                    print("Nenhum livro encontrado")

            except:
                print(
                    "Ocorreu um erro ao tentar buscar o livro, verefique o titulo ou se o livro existe"
                )

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
