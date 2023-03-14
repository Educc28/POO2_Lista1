def main():
    num = int(input("Digite um numero para fatorar: "))
    result = 1

    if num == 0:
        print("0! = 1")
    else:
        print(f"{num}! = {num}", end= " ")
        for i in range(1, num+1):
            result = result * i
            if i != num:
                print(f". {num-i}", end=" ")
        print(f" = {result}")


main()
