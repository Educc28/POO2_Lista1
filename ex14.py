def main():
    numPar = 0
    numImpar = 0
    for i in range(10):
        num = int(input("Digite um numero: "))
        if(num % 2 == 0):
            numPar += 1
        else:
            numImpar += 1
    print(f"A quantidade de numeros pares e: {numPar}")
    print(f"A quantidade de numeros impares e: {numImpar}")


main()
