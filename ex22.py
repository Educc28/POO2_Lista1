def main():
    num = int(input("Digite um numero inteiro: "))
    naoPrimo = False
    for i in range(1, num+1):
        result = num % i
        if num == 1:
            naoPrimo = True
            break
        elif result == 0 and i != 1 and i != num:
            print(f"O numero e divisivel por {i}")
            naoPrimo = True
            continue

    if naoPrimo == True and num != 1:
        print(f"Logo, o numero {num} nao e primo")
    elif naoPrimo == True and num == 1:
        print(f"O numero {num} nao e primo")
    else:
        print(f"O numero {num} e primo")


main()
