#From | Import

from AppComPOO.produto import Produto
from AppComPOO.avaliacao import Avaliacao

produto_virtual = Produto('Blusa', 'Vestuario')
produto_fastfood = Produto('Batatas', 'Comida')
produto_eletronico = Produto ('celular', 'smartphone')

produto_virtual.receber_avaliacao('Jose', 10)
produto_virtual.receber_avaliacao('Maria', 9)

produto_virtual.alternar_estado()

def main():
    Produto.listar_produtos()

if __name__ == '__main__':
    main()