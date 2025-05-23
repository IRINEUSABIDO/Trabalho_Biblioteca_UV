import json
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, ID, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.ID = ID
        self.status = status

    def editar_livro(self, novo_titulo, novo_autor, novo_ano_publicacao):
        pass

    def marcar_como_emprestado(self):
        pass
    
    def marcar_como_disponivel(self):
        pass

class Biblioteca:
    def __init__(self, nome="Alex Library"):
        self.nome = nome

    def adicionar_livro(self, livro):
        #save_to_json
        livroDict = {
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "id": livro.ID,
            "status": livro.status
        }
        with open("livros.json", "w") as f:
            f.write(json.dumps(livroDict, indent=1))

    def remover_livro(self, livro):
        pass

    def listar_livros(self):
        #load_from_json
        with open("livros.json", "r") as f:
            data = json.loads(f.read())
            if data == "":
                print("Nenhum livro cadastrado")
            else:
                for x in range(1):
                    print(f"ID: {data['id']}")
                    print(f"Título: {data['titulo']}")
                    print(f"Autor: {data['autor']}")
                    print(f"Ano de Publicação: {data['ano_publicacao']}")
                    print(f"Status: {data['status']}",end="\n\n")

    def buscar_livro(self, titulo):
        pass

