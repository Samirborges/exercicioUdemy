import packagesExercicio
import packageInterface

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10% - CUMPRIDO

# Gere novos_produtos por deep copy (cópia profunda) - CUMPRIDO
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor) - CUMPRIDO
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda) - CUMPRIDO

# Ordene os produtos por preco crescente (do menor para maior) 
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# print(produtos[0]['preco'])


porcentagem = 10

packagesExercicio.atualizarPreco(produtos, porcentagem)
print(f'Aumento de preços em {porcentagem}')
packagesExercicio.mostraProdutos(produtos)
while True:
    listaOpcoes = ['Cadastrar novo produto', 'Ver todos os produtos', 'Listar em ordem crescente', 'Listar em ordem decrescente', 'Listar em ordem de preço', 'Sair']
    choiceUser = packageInterface.menuOptions(listaOpcoes, True)

    newProdut = produtos.copy()
    match choiceUser:
        case 1:
            newProdut = packagesExercicio.cadastrarNovoProduto(newProdut, porcentagem)
            packagesExercicio.mostraProdutos(newProdut)
            
        case 2:
            packagesExercicio.mostraProdutos(newProdut)

        case 3:
            print('Produtos ordenados de forma crescente')
            listaCrescente = packagesExercicio.listaOrdenada(newProdut, 'c')
            packagesExercicio.mostraProdutos(listaCrescente)
        
        case 4:
            # Lista de ordem decrescente
            print('Produtos orndenados de forma decrescente')
            listaDecrescente = packagesExercicio.listaOrdenada(newProdut, 'd')
            packagesExercicio.mostraProdutos(listaDecrescente)

        case 5:    
            # Lista ordenada de forma crescente pelos preços
            print('Produtos ordenados por preços')
            listaCrescentePreco = packagesExercicio.listaOrdenaPreco(newProdut)
            packagesExercicio.mostraProdutos(listaCrescentePreco)

        case 6:
            break