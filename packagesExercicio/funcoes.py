def aumentaPreco(preco, porc):
    valorAumenta = porcentagem(porc)
    novo_preco = preco+(preco*valorAumenta)
    return novo_preco
    

def porcentagem(porc):
    porcentagem = porc/100
    return porcentagem


def atualizarPreco(produtos, porc):
    for produto in produtos:
        valor_produto = aumentaPreco(produto['preco'], porc)
        produto['preco'] = valor_produto
    
          
def cadastrarNovoProduto(listProdutos, porcent):
    nomeProduto = str(input('Nome: '))
    precoProduto = aumentaPreco(float(input('Preço: R$')), porcent)
    
    novoProduto = {'nome':nomeProduto, 'preco':precoProduto}
    listProdutos.append(novoProduto)
    return listProdutos
    

def mostraProdutos(produtos):
    print('-'*40)
    print('Produtos \t\t Preços')
    for produt in produtos:
        print(f'Nome: {produt['nome']} \t preço R${produt['preco']:.2f}\n')
    print('-'*40)