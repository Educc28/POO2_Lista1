def main():
    i = 1
    Pao = float(input("Digite o preco do pao: "))
    while i < 51:
        valor = i * Pao
        print(f"{i} - R${valor}")
        i += 1

main()
