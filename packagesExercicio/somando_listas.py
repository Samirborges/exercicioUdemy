# Exercício de soma de listas, considerando que irá fundir com a lista menor
lista1 = [10, 2, 3, 40, 5, 6, 7]
lista2 = [1, 2, 3, 4]
lista_soma = [elemA + elemB for elemA, elemB in zip(lista1, lista2)]
print(lista_soma)