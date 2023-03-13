def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    num = int(input("Digite seu numero: "))

    for i in range(num):
        print(fibonacci(i))


main()
