import json
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, id, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.id = id
        self.status = status

    def editar_livro(self, novo_titulo, novo_autor, novo_ano_publicacao):
        pass

    def marcar_como_emprestado(self):
        pass
    
    def marcar_como_disponivel(self):
        pass

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        pass

    def remover_livro(self, livro):
        #save_to_json
        pass

    def listar_livros(self):
        #load_from_json
        pass

    def buscar_livro(self, titulo):
        pass

