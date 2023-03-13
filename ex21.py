def main():
    num = int(input("Digite um numero inteiro: "))

    for i in range(1, num+1):
        result = num % i
        if num == 1:
            print("O numero nao e primo")
            break
        elif result == 0 and i != 1 and i != num:
            print("O numero nao e primo")
            break
        elif i != num:
            continue
        else:
            print("O numero e primo")
            break


main()
