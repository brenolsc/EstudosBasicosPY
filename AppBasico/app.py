import os

produtos = [{'Nome': 'Blusa', 'Categoria':'Vestuário', 'Ativo':False},
                {'Nome': 'Bota', 'Categoria':'Calçado', 'Ativo':True},
                {'Nome': 'Anel', 'Categoria':'Bijuteria', 'Ativo':False}                
]

def exibir_nome_do_programa():
    print('🅰 🅿 🅿')

def exibir_opcoes():
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Ativar/Desativar Produto')
    print('4. Sair')
    
def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    
def opcao_invalida():
    print('Essa opção não é válida\n')
    voltar_menu_principal()
    
def cadastrar_novo_produto():
    exibir_subtitulos('Cadastro de novos produtos\n')
    nome_do_produto = input('Digite o nome do produto que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_produto}: ')
    dados_do_produto = {'Nome':nome_do_produto,
                            'Categoria':categoria,
                            'Ativo':False
    }
    produtos.append(dados_do_produto)
    print(f'o {nome_do_produto} foi cadastrado com sucesso!')
    
    voltar_menu_principal()

def listar_produtos():
    exibir_subtitulos('Listando Produtos')
    
    print(f'{'Nome do Produto'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for produto in produtos:
        nome_produto = produto['Nome']
        categoria = produto['Categoria']
        ativo = 'Ativado!' if produto['Ativo'] else 'Desativado!'
        print(f'- {nome_produto.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_menu_principal()
    
def alternar_estado_produto():
    exibir_subtitulos('Alterando estado do produto\n')
    nome_produto = input('Digite o nome do produto que deseja alternar o estado: ')
    produto_encontrado = False
    
    for produto in produtos:
        if nome_produto == produto['Nome']:
            produto_encontrado = True
            produto['Ativo'] = not produto['Ativo']
            mensagem = f'O produto{nome_produto} foi ativo com sucesso' if produto['Ativo'] else f'O produto {nome_produto} foi desativado com sucesso'
            print(mensagem)
    if not produto_encontrado:
        print('produto não encontrado, verifique as letras maiúsculas e minúsculas!')
        
    voltar_menu_principal()
    
def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        def encerrar_app():
            exibir_subtitulos('finalizando APP\n')

        if opcao_escolhida == 1:
            cadastrar_novo_produto()

        elif opcao_escolhida == 2:
            listar_produtos()

        elif opcao_escolhida == 3:
            alternar_estado_produto()
        
        elif opcao_escolhida == 4:
            encerrar_app()
        
        else:
            opcao_invalida()          
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()