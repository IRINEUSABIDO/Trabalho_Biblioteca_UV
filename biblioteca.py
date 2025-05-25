import json


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, ID, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.ID = ID
        self.status = status

    def marcar_como_emprestado(self):
        self.status = "Emprestado"

    def marcar_como_disponivel(self):
        self.status = "Disponivel"


class Biblioteca:
    def __init__(self, nome="Alex Library"):
        self.nome = nome

    def adicionar_livro(self, livro):
        livroDict = {
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "id": livro.ID,
            "status": livro.status,
        }
        with open("livros.json", "r") as f:
            data = json.loads(f.read())

        data["lista_livros"].append(livroDict)

        with open("livros.json", "w") as f:
            f.write(json.dumps(data, indent=1))

    def remover_livro(self, livroID):
        with open("livros.json", "r") as f:
            data = json.loads(f.read())
            nova_data = [
                livro for livro in data["lista_livros"] if livro["id"] != livroID
            ]

        if nova_data == data["lista_livros"]:
            return False

        else:
            data["lista_livros"] = nova_data
            with open("livros.json", "w") as f:
                f.write(json.dumps(data, indent=1))
            return True

    def editar_livro(self, novo_titulo, novo_autor, novo_ano_publicacao, livroID):
        with open("livros.json", "r") as f:
            data = json.loads(f.read())

        with open("livros.json", "r") as f:
            data2 = json.loads(f.read())

        for livro in data["lista_livros"]:
            if livro["id"] == livroID:
                livro["titulo"] = novo_titulo
                livro["autor"] = novo_autor
                livro["ano_publicacao"] = novo_ano_publicacao

        if data["lista_livros"] == data2["lista_livros"]:
            return "Livro não encontrado"
        else:
            with open("livros.json", "w") as f:
                f.write(json.dumps(data, indent=1))

            return "Livro editado com sucesso"

    def listar_livros(self):
        with open("livros.json", "r") as f:
            data = json.loads(f.read())
            if data == "":
                print("Nenhum livro cadastrado")
            else:
                for livro in data["lista_livros"]:
                    print(f"ID: {livro['id']}")
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Ano de Publicação: {livro['ano_publicacao']}")
                    print(f"Status: {livro['status']}", end="\n\n")

    def buscar_livro(self, titulo):
        livro_encontrado = False
        with open("livros.json", "r") as f:
            data = json.loads(f.read())
            for livro in data["lista_livros"]:
                if livro["titulo"] == titulo:
                    print(f"ID: {livro['id']}")
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Ano de Publicação: {livro['ano_publicacao']}")
                    print(f"Status: {livro['status']}", end="\n\n")
                    livro_encontrado = True
        return livro_encontrado

    def gerar_relatorio(self):
        Disponivel = 0
        Emprestado = 0
        with open("livros.json", "r") as f:
            data = json.loads(f.read())
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
            with open("livros.json", "r") as f:
                data = json.loads(f.read())

            for livro in data["lista_livros"]:
                if livro["id"] == livroID and livro["status"] == "Disponivel":
                    livro["status"] = "Emprestado"
                    with open("livros.json", "w") as f:
                        f.write(json.dumps(data, indent=1))

                    return "Livro emprestado com sucesso" 

                elif livro["id"] == livroID and livro["status"] == "Emprestado":
                    livro["status"] = "Disponivel"
                    with open("livros.json", "w") as f:
                        f.write(json.dumps(data, indent=1))

                    return "Livro devolvido com sucesso"
        except:
            print("Ocorreu um erro ao tentar mudar o status do livro")

        return "Livro não encontrado"
