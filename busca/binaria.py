def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]

        if valor_meio == elemento:
            return meio  # Retorna o índice do elemento encontrado
        elif valor_meio < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  # Retorna -1 se o elemento não for encontrado

# Exemplo de uso
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_busca = 3
indice = busca_binaria(minha_lista, elemento_busca)

if indice != -1:
    print(f'O elemento {elemento_busca} foi encontrado no índice {indice}.')
else:
    print(f'O elemento {elemento_busca} não foi encontrado na lista.')
