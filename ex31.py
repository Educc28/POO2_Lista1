def main():
    compras = []
    i = 1
    listElement = -1
    dinheiro = 0

    while listElement != 0:
        listElement = float(input((f"Produto {i}: R$ ")))
        compras.append(listElement)
        i += 1


    comprasTotal = sum(compras)
    print(f"Total: {comprasTotal}")

    while dinheiro < comprasTotal:
        dinheiro = float(input("Dinheiro: R$ "))
        if dinheiro < comprasTotal:
            print("Dinheiro insuficiente, tente novamente")
            dinheiro = float(input("Dinheiro: R$ "))
        else:
            break
    
    print("Troco: R$ ", dinheiro-comprasTotal)

main()
