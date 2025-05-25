import json
def verificar_ano_de_publicacao(ano_de_publicacao) -> bool:
    if ano_de_publicacao.isnumeric() and int(ano_de_publicacao) > 0:
        return True
    else:
        return False
    
def verificar_id(id) -> bool:
    if id.isnumeric() and len(id) == 4:
        return True
    else:
        return False

def exibir_informacoes(livro):
    print(f"ID: {livro['id']}")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano de Publicação: {livro['ano_publicacao']}")
    print(f"Status: {livro['status']}", end="\n\n")

def mudar_status(livro,livroID):
    if livro["id"] == livroID and livro["status"] == "Disponivel":
        return "Emprestado", "Livro emprestado com sucesso"
    
    elif livro["id"] == livroID and livro["status"] == "Emprestado":
        return "Disponivel", "Livro devolvido com sucesso"

def criar_dados():
    data = {
        "lista_livros": []
    }
    with open("livros.json", "w") as f:
        f.write(json.dumps(data, indent=1))


def ler_dados() -> dict | bool: 
    try:
        with open ("livros.json", "r") as f:
            data = json.loads(f.read())
        return data
    
    except FileNotFoundError:
        return False
    
def salvar_dados(data):
    with open("livros.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=1, ensure_ascii=False))