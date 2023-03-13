def potencia(base, expoente):
    resultado = base
    if expoente == 0:
        print(1)
        return

    for i in range(1, expoente):
        resultado = base * resultado
    print(resultado)


def main():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    potencia(base, expoente)


main()
