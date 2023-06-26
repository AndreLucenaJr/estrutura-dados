def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]

        if valor_meio == elemento:
            return meio  
        elif valor_meio < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1 