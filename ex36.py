def tabuada(n, inicio, final):
    
    for i in range(inicio, final+1):
        print(f"{n} x {i} = {n * i}")


def main():
    num = int(input("Digite um numero para ver sua tabuada: "))
    inicio = int(input("Começar por: "))
    final = int(input("Terminar em: "))
    while inicio >= final:
        print("O inicio nao pode ser maior que o final, tente novamente")
        inicio = int(input("Começar por: "))
        final = int(input("Terminar em: "))
    tabuada(num, inicio, final)


main()
