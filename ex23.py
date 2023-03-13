def main():
    num = int(input("Digite um numero inteiro: "))
    counter = 0

    print("Os numeros primos sao: ")
    for n in range(1, num+1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    counter += 1
                    break
            else:
                counter += 1
                print(n)
    print(f"foram feitas {counter} divisoes")


main()
