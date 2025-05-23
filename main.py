from biblioteca import Biblioteca, Livro
import random
nomeBiblioteca = input("Digite o nome da biblioteca: ")
biblioteca = Biblioteca(nomeBiblioteca)

def main():
    print("\nGerenciador de Biblioteca\n" )
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

            
            randomID = str(random.randint(1000, 9999))
            NovoLivro = Livro(livroTitulo, livroAutor, livroAnoDePublicacao, randomID,"Disponivel")
            biblioteca.adicionar_livro(NovoLivro)

        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
