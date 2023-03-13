def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    for i in range(1000):
        n = fibonacci(i)
        print(fibonacci(i))
        if n > 500:
            break


main()
