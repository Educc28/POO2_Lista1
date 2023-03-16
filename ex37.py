def main():
    clients = {}
    code = -1
    height = -1
    weight = -1

    while code != 0:
        code = int(input("Digite seu codigo: "))
        if code == 0:
            break
        else:
            height = float(input("Digite sua altura: "))
            weight = float(input("Digite seu peso: "))
        clients[code] = [height, weight]



    # print(clients)


main()
