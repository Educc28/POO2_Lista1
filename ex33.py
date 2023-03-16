import statistics

def main():
    listSize = int(input("Digite quantas temperaturas voce quer colocar: "))
    list1 = []

    for i in range(1, listSize+1):
        listElement = float(input("Digite um numero: "))
        list1.append(listElement)
    print("O menor valor e: ", min(list1))
    print("O maior valor e: ", max(list1))
    print("A media dos valores e: ", statistics.mean(list1))


main()
