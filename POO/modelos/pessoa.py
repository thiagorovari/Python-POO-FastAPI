class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._profissao = ''
    
    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._idade} anos | {self._profissao}'
    
    def aniversario(self):
        self._idade = self._idade + 1
    
    def saudacao(self):
        if self._profissao == '' : 
            print(f"Olá! Me chamo {self._nome} e estou desempregado 😭" )
        else: 
            print( f"Olá! Me chamo {self._nome} e sou {self._profissao}")

thiago = Pessoa("Thiago", 20)
lucas = Pessoa("Lucas" , 17)
pai = Pessoa("Hebert", 56)

print(lucas)
print(thiago)
lucas.aniversario()
print(lucas)
pai._profissao = "engenheiro"
pai.saudacao()
lucas.saudacao()