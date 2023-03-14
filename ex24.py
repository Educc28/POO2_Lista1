import statistics

def main():
    listSize = int(input("Digite quantos numeros voce quer colocar: "))
    list1 = []

    for i in range(1, listSize+1):
        listElement = int(input("Digite um numero: "))
        list1.append(listElement)

    print("A media dos valores e: ", statistics.mean(list1))

main()
