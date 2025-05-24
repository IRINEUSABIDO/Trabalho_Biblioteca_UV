import json


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, ID, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.ID = ID
        self.status = status

    def marcar_como_emprestado(self):
        pass

    def marcar_como_disponivel(self):
        pass


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
            return False
        else:
            with open("livros.json", "w") as f:
                f.write(json.dumps(data, indent=1))

            return True

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
