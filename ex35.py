def main():
    num = int(input("Digite um numero inteiro: "))

    print("Os numeros primos sao: ")
    for n in range(1, num+1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)


main()
