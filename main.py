import time
from Organizacao_dados.Bubble_Sort import *
from Organizacao_dados.Heap_Sort import *
from Organizacao_dados.Insert_Sort import *
from Organizacao_dados.Merge_Sort import *
from Organizacao_dados.Quick_Sort import *
from Organizacao_dados.Select_Sort import *
from util.DataEnum import *

def loadArr(data: Data):
    with open(f'data/{data.value}.txt','r') as f:
                list = []
                contents = f.read()
                arr = contents.split("\n")
                arr.pop()
                for num in arr:
                    list.append(int(num))
                return list

def performanceAnalysis(func, qnt):
    list = loadArr(qnt)

    start = time.time()

    func(list)

    final = time.time()
    print(final - start)

def chooseQuantity():
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


while True:
    print("Opções:")
    print("1 - Bubble sort")
    print("2 - Heap sort")
    print("3 - Insert sort")
    print("4 - Merge sort")
    print("5 - Quick sort")
    print("6 - Select sort")
    print("0 - Cancelar operação")
    option = input("Digite o número desejado\t")

    match option:
        case "1":
            qnt = chooseQuantity()
            performanceAnalysis(bubbleSort, qnt)
        case "2":
            qnt = chooseQuantity()
            performanceAnalysis(heapSort, qnt)
        case "3":
            qnt = chooseQuantity()
            performanceAnalysis(insertionSort, qnt)
        case "4":
            qnt = chooseQuantity()
            performanceAnalysis(mergeSort, qnt)
        case "5":
            qnt = chooseQuantity()
            performanceAnalysis(quick_sort, qnt)
        case "6":
            qnt = chooseQuantity()
            performanceAnalysis(selection_sort, qnt)
        case "0":
            break
        case _:
            print("Comando não encontrado")

