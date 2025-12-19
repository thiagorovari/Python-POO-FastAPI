from POO.cardapio.item_carcapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self):
        #print(f"{'Bebida'.ljust(25)} | {'Preco'.ljust(25)} | 'Tamanho'")
        #print(f' {self._nome.ljust(25)} | {str(self._preco).ljust(25)} |{self._tamanho} ') ERRO NO PRINT
        return self._nome
    