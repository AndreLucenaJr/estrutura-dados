import time
from Organizacao_dados.Bubble_Sort import *
from Organizacao_dados.Heap_Sort import *
from Organizacao_dados.Insert_Sort import *
from Organizacao_dados.Merge_Sort import *
from Organizacao_dados.Quick_Sort import *
from Organizacao_dados.Select_Sort import *
from Estruturas_Busca.Arvore_AVL import *
from Estruturas_Busca.arvoreBinaria import *
from Estruturas_Busca.sequencial import *
from Estruturas_Busca.binaria import *
from util.DataEnum import *

bst = BinarySearchTree()
avl = AVLTree()
arr = []


def loadArr(data: Data):
    with open(f'data/{data.value[1]}.txt', 'r') as f:
        list = []
        contents = f.read()
        arr = contents.split("\n")
        arr.pop()
        for num in arr:
            list.append(int(num))
        return list


def performanceSortAnalysis(func, qnt):
    list = loadArr(qnt)

    start = time.time()

    func(list)

    final = time.time()
    print(f"## A operação durou {final - start} segundos. ##")


def performanceTreeSearchAnalysis(func, value):
    start = time.time()

    func(value)

    final = time.time()
    print(f"## A operação durou {final - start} segundos. ##")


def performanceBinarySearchAnalysis(func, value, list):
    start = time.time()

    result = func(list, value)
    if result != -1:
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')

    final = time.time()
    print(f"## A operação durou {final - start} segundos. ##")


def performanceSearchAnalysis(func, value, qnt):
    list = loadArr(qnt)
    start = time.time()

    result = func(list, value)
    if result != -1:
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')

    final = time.time()
    print(f"## A operação durou {final - start} segundos. ##")


def createBinaryTree(list):
    global bst
    for num in list:
        bst.insert(num)


def createAvlTree(list):
    global avl
    for num in list:
        avl.insert(num)


def searchBinaryTree(value):
    global bst
    result = bst.search(value)
    if result:
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')


def searchAvlTree(value):
    global avl
    result = avl.search(value)
    if result:
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')


def chooseQuantity():
    print("=======================================================")
    print("Opções:")
    print("1 - MIL")
    print("2 - DEZ MIL")
    print("3 - CEM MIL")
    print("4 - UM MILHÃO")
    quantity = input("Quantos números você deseja utilizar?\t")

    match quantity:
        case "1":
            return Data.MIL
        case "2":
            return Data.DEZ_MIL
        case "3":
            return Data.CEM_MIL
        case "4":
            return Data.MILHAO


def sortMethods():
    while True:
        print("=======================================================")
        print("Opções:")
        print("1 - Bubble sort")
        print("2 - Heap sort")
        print("3 - Insert sort")
        print("4 - Merge sort")
        print("5 - Quick sort")
        print("6 - Select sort")
        print("7 - Árvore binária")
        print("8 - Árvore AVL")
        print("0 - Cancelar operação")
        option = input("Qual método de ordenação você quer utilizar?\t")
        match option:
            case "1":
                qnt = chooseQuantity()
                performanceSortAnalysis(bubbleSort, qnt)
                continue
            case "2":
                qnt = chooseQuantity()
                performanceSortAnalysis(heapSort, qnt)
                continue
            case "3":
                qnt = chooseQuantity()
                performanceSortAnalysis(insertionSort, qnt)
                continue
            case "4":
                qnt = chooseQuantity()
                performanceSortAnalysis(mergeSort, qnt)
                continue
            case "5":
                qnt = chooseQuantity()
                performanceSortAnalysis(quick_sort, qnt)
                continue
            case "6":
                qnt = chooseQuantity()
                performanceSortAnalysis(selection_sort, qnt)
                continue
            case "7":
                qnt = chooseQuantity()
                performanceSortAnalysis(createBinaryTree, qnt)
                continue
            case "8":
                qnt = chooseQuantity()
                performanceSortAnalysis(createAvlTree, qnt)
                continue
            case "0":
                break
            case _:
                print("Comando não encontrado")


def searchMethod():
    while True:
        print("=======================================================")
        print("1 - Busca binária")
        print("2 - Busca sequencial")
        print("3 - Busca árvore binária")
        print("4 - Busca árvore AVL")
        print("0 - Cancelar operação")
        option = input("Qual método de busca você quer utilizar?\t")
        match option:
            case "1":
                qnt = chooseQuantity()
                value = int(input("Qual valor você deseja pesquisar?\t"))
                global arr
                if len(arr) != qnt.value[0]:
                    list = quick_sort(loadArr(qnt))
                    arr = list
                performanceBinarySearchAnalysis(busca_binaria, value, arr)
            case "2":
                qnt = chooseQuantity()
                value = int(input("Qual valor você deseja pesquisar?\t"))
                performanceSearchAnalysis(busca_sequencial, value, qnt)
            case "3":
                print("Lembrando: É preciso criar a árvore primeiro no método de ordenação")
                value = int(input("Qual valor você deseja pesquisar?\t"))
                performanceTreeSearchAnalysis(searchBinaryTree, value)
            case "4":
                print("Lembrando: É preciso criar a árvore primeiro no método de ordenação")
                value = int(input("Qual valor você deseja pesquisar?\t"))
                performanceTreeSearchAnalysis(searchAvlTree, value)
            case "0":
                break
            case _:
                print("Comando não encontrado")


def compareMethods():
    while True:
        print("=======================================================")
        print("Opções:")
        print("1 - Comparar métodos de ordenação")
        print("2 - Comparar métodos de busca")
        print("0 - Cancelar operação")
        option = input("Qual método de comparação você deseja utilizar?\t")
        match option:
            case "1":
                qnt = chooseQuantity()
                value = int(input("Qual valor você deseja pesquisar?\t"))
                list = loadArr(qnt)
                start = time.time()
                bubbleSort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Bubble Sort: {end - start} segundos.")

                start = time.time()
                insertionSort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Insertion Sort: {end - start} segundos.")

                start = time.time()
                selection_sort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Selection Sort: {end - start} segundos. ")

                start = time.time()
                mergeSort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Merge Sort: {end - start} segundos. ")

                start = time.time()
                quick_sort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Quick Sort: {end - start} segundos. ")

                start = time.time()
                heapSort(list.copy())
                end = time.time()
                print(f"Tempo de execução do Heap Sort: {end - start} segundos. ")

                start = time.time()
                createBinaryTree(list.copy())
                end = time.time()
                print(f"Tempo de execução da criação da Árvore Binária: {end - start} segundos. ")

                start = time.time()
                createAvlTree(list.copy())
                end = time.time()
                print(f"Tempo de execução da criação da Árvore AVL: {end - start} segundos. ")

                continue
            case "2":
                qnt = chooseQuantity()
                value = int(input("Qual valor você deseja pesquisar?\t"))
                list = quick_sort(loadArr(qnt))
                start = time.time()
                busca_binaria(list.copy(), value)
                end = time.time()
                print(f"Tempo de execução da Busca Binária: {end - start} segundos. ")

                start = time.time()
                busca_sequencial(list.copy(), value)
                end = time.time()
                print(f"Tempo de execução da Busca Sequencial: {end - start} segundos. ")

                createBinaryTree(list.copy())
                start = time.time()
                searchBinaryTree(value)
                end = time.time()
                print(f"Tempo de execução da busca na Árvore Binária: {end - start} segundos. ")

                createAvlTree(list.copy())
                start = time.time()
                searchAvlTree(value)
                end = time.time()
                print(f"Tempo de execução da busca na Árvore AVL: {end - start} segundos. ")

                continue
            case "0":
                break
            case _:
                print("Comando não encontrado")


if __name__ == '__main__':
    while True:
        print("=======================================================")
        print("1 - Ordenação")
        print("2 - Busca")
        print("3 - Comparação")
        print("0 - Cancelar operação")
        option = input("Qual método você deseja?\t")
        match option:
            case "1":
                sortMethods()
            case "2":
                searchMethod()
            case "3":
                compareMethods()
            case "0":
                break
            case _:
                print("Comando não encontrado")
