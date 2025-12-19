from typing import List
from POO.modelos.avaliacao import Avaliacao
from POO.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes: List['Restaurante'] = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(12)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(12)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self): 
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def add_item_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f"Cardapio do Restuarante {self._nome}")
        for i in range(len(self._cardapio)):
            print(f"{'Nome do item '.ljust(25)} | {'Preco'.ljust(25)} |")
            print(f"{self._cardapio[i]._nome.ljust(25)} | R$:{str(self._cardapio[i]._preco).ljust(25)} \n")
    



