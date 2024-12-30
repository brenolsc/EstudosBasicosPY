#Metodos

from AppComPOO.avaliacao import Avaliacao


class Produto:
    produtos = []
    
    def __init__ (self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Produto.produtos.append(self)   
        
# Parte textual do objeto
    def __str__ (self):
            return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_produtos(cls):
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(25)} | {produto._categoria.ljust(25)} | {str(produto.media_avaliacoes).ljust(25)} |{produto.ativo}')
        
    @property
    def ativo(self):
        return 'ativado' if self._ativo else 'desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao (cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return ''
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media
