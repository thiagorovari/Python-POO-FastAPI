from POO.modelos.restaurante import Restaurante
from POO.cardapio.bebida import Bebida
from POO.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_praca.receber_avaliacao('Gui', 10)
#restaurante_praca.receber_avaliacao('Lais', 8)
#restaurante_praca.receber_avaliacao('Emy', 2)

suco_laranja = Bebida('suco de laranja', 11, 700)
parmegiana = Prato('Parmegiana de Frango', 200, 'Bife de frnago a parmegiana')

def main():
    print(suco_laranja)
    print(parmegiana)

if __name__ == '__main__':
    main()