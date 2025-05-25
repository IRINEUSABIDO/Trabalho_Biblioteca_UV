from biblioteca import Biblioteca, Livro
import utils 
import random
import sys

biblioteca = Biblioteca("Alex Library")


def adicionar_livro():
    livroTitulo = input("Digite o título do livro: ")
    livroAutor = input("Digite o autor do livro: ")
    livroAnoDePublicacao = input("Digite o ano de publicação do livro: ")

    if utils.verificar_ano_de_publicacao(livroAnoDePublicacao):
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

    else:
        print("Ano de publicação inválido")


def listar_livros():
    biblioteca.listar_livros()


def editar_livro():
    livro_ID = input("Digite o ID do livro que deseja editar: ")

    if utils.verificar_id(livro_ID) == False:
        print("Digite um ID valido")
        return False

    livro_novo_titulo = input("Digite o novo título do livro: ")
    livro_novo_autor = input("Digite o novo autor do livro: ")
    livro_novo_ano_de_publicacao = input("Digite o novo ano de publicação do livro: ")

    if utils.verificar_ano_de_publicacao(livro_novo_ano_de_publicacao) == False:
        print("Digite um ano de publicaçao valido")
        return False

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


def excluir_livro():
    livroID = input("Digite o ID do livro que deseja excluir: ")

    if utils.verificar_id(livroID) == False:
        print("Digite um numero de ID valido")
        return False

    try:
        print(biblioteca.remover_livro(livroID))

    except:
        print("Ocorreu um erro ao tentar excluir o livro")


def buscar_livro():
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


def gerar_relatorio():
    biblioteca.gerar_relatorio()


def gerenciar_status():
    livroID = input("Digite o ID do livro que deseja mudar o status: ")
    if utils.verificar_id(livroID) == False:
        print("Digite um numero de ID valido")
        return False

    print(biblioteca.gerenciar_status(livroID))


def sair():
    print("Saindo...")
    sys.exit()
