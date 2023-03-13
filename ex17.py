def main():
    num = int(input("Digite um numero para fatorar: "))
    result = 1

    if num == 0:
        print("O fatorial e: 1")
    else:
        for i in range(1, num+1):
            result = result * i
        print(f"O fatorial de {num} e: {result}")


main()
