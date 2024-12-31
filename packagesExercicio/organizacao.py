def listaOrdenada(listProdut, ordena):  
    listBackup = list()
    for produto in listProdut:
        listBackup.append(int(produto['nome'][8]))
    
    listaOrdenada = list()
    while len(listBackup) != 0:
        listBackup = sorted(listBackup)
        if ordena == 'd':
            indice = listBackup[-1]
        elif ordena == 'c':
            indice = listBackup[0]
    
        for produt in listProdut:
            if indice == int(produt['nome'][8]):
                listaOrdenada.append(produt)
                listBackup.remove(indice)
    
    return listaOrdenada


def listaOrdenaPreco(listProdut):
    listBackup = list()
    for precoProduto in listProdut:
        listBackup.append(precoProduto['preco'])
    
    listBackup = sorted(listBackup)
    listaOrdenada = list()
    while len(listBackup) != 0:
        menorPreco = listBackup[0]
        
        for produt in listProdut:
            if menorPreco == produt['preco']:
                listaOrdenada.append(produt)
                listBackup.remove(menorPreco)
        
    return listaOrdenada
            