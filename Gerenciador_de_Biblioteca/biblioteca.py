import utils

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, ID, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.ID = ID
        self.status = status


class Biblioteca:
    def __init__(self, nome="Alex Library"):
        self.nome = nome

        if utils.ler_dados() == False:
            utils.criar_dados()

    def adicionar_livro(self, livro):
        livroDict = {
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "id": livro.ID,
            "status": livro.status,
        }

        data = utils.ler_dados()
        if data == False:
            return "Não foi possível adicionar o livro"

        data["lista_livros"].append(livroDict)

        utils.salvar_dados(data)

        return "Livro adicionado com sucesso"

    def remover_livro(self, livroID):
        data = utils.ler_dados()
        nova_data = [livro for livro in data["lista_livros"] if livro["id"] != livroID]

        if nova_data == data["lista_livros"]:
            return "Livro não encontrado"

        else:
            data["lista_livros"] = nova_data
            utils.salvar_dados(data)
            return "Livro removido com sucesso"

    def editar_livro(self, novo_titulo, novo_autor, novo_ano_publicacao, livroID):
        data = utils.ler_dados()
        data2 = utils.ler_dados()

        for livro in data["lista_livros"]:
            if livro["id"] == livroID:
                livro["titulo"] = novo_titulo
                livro["autor"] = novo_autor
                livro["ano_publicacao"] = novo_ano_publicacao

        if data["lista_livros"] == data2["lista_livros"]:
            return "Livro não encontrado"

        else:
            utils.salvar_dados(data)
            return "Livro editado com sucesso"

    def listar_livros(self):
        data = utils.ler_dados()

        if len(data["lista_livros"]) == 0:
            print("Nenhum livro cadastrado")

        else:
            for livro in data["lista_livros"]:
                utils.exibir_informacoes(livro)

    def buscar_livro(self, titulo) -> bool:
        livro_encontrado = False
        data = utils.ler_dados()

        for livro in data["lista_livros"]:
            if livro["titulo"] == titulo:
                utils.exibir_informacoes(livro)
                livro_encontrado = True

        return livro_encontrado

    def gerar_relatorio(self):
        Disponivel = 0
        Emprestado = 0
        data = utils.ler_dados()
        print("Relatório de Livros")
        print(f"Quantidade de Livros: {len(data['lista_livros'])}")

        for i in data["lista_livros"]:
            if i["status"] == "Disponivel":
                Disponivel += 1

            else:
                Emprestado += 1

        print(f"Quantidade de Livros Disponíveis: {Disponivel}")
        print(f"Quantidade de Livros Emprestados: {Emprestado}")

    def gerenciar_status(self, livroID):
        try:
            data = utils.ler_dados()

            for livro in data["lista_livros"]:
                    if livro["id"] == livroID:
                        novo_status = utils.mudar_status(livro,livroID)
                        livro["status"] = novo_status[0]
                        utils.salvar_dados(data)

                        return novo_status[1]
        except:
            print("Ocorreu um erro ao tentar mudar o status do livro")
            return False

        return "Livro não encontrado"
