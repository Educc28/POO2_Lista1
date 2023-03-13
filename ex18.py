def main():
    listSize = int(input("Digite quantos numeros voce quer colocar: "))
    list1 = []

    for i in range(1, listSize+1):
        listElement = int(input("Digite um numero: "))
        list1.append(listElement)
    print("O menor valor e: ", min(list1))
    print("O maior valor e: ", max(list1))
    print("A soma dos valores e: ", sum(list1))


main()
