from util.DataEnum import *
import time

def loadArr(data: Data):
    with open(f'data/{data.value[1]}.txt', 'r') as f:
        list = []
        contents = f.read()
        arr = contents.split("\n")
        arr.pop()
        for num in arr:
            list.append(int(num))
        return list


def performanceMethodAnalysis(func, list, methodName):
    start = time.time()
    func(list)
    end = time.time()
    print(f"Tempo de execução {methodName}: {end - start} segundos.")

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