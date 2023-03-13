def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def main():
    num = int(input("Digite um numero para ver sua tabuada: "))
    tabuada(num)


main()
