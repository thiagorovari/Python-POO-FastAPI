from numpy import random

def verifica_estoque():
    livros = random.randint(10)
    print(f"Numero de livros em estoque:{livros}\n")
    for i in range(livros):
        print(f"Venda realizada! Estoque restante:{livros}")
        livros = livros - 1
    print("Estoque esgotado...")


def filtro_livros(livros):
    for livro in livros:
        if livro['estoque'] > 0:
            print(f"Livro dispoivel em estoque: {livro['nome']}.")
        else:
            continue

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

filtro_livros(livros)

###verifica_estoque()
