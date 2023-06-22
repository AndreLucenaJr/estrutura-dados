def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i 
    return -1  


minha_lista = [10, 5, 8, 3, 2, 6, 1, 4, 7, 9]
elemento_busca = 6
indice = busca_sequencial(minha_lista, elemento_busca)

if indice != -1:
    print(f'O elemento {elemento_busca} foi encontrado no índice {indice}.')
else:
    print(f'O elemento {elemento_busca} não foi encontrado na lista.')
