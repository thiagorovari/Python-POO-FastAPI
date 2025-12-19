from POO.modelos.restaurante import Restaurante
from POO.cardapio.bebida import Bebida
from POO.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_praca.receber_avaliacao('Gui', 10)
#restaurante_praca.receber_avaliacao('Lais', 8)
#restaurante_praca.receber_avaliacao('Emy', 2)

suco_laranja = Bebida('suco de laranja', 11, '700ml')
parmegiana = Prato('Parmegiana de Frango', 200, 'Bife de frnago a parmegiana')
restaurante_praca.add_item_cardapio(suco_laranja)
restaurante_praca.add_item_cardapio(parmegiana)

def main():
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()