import statistics

def main():
    a = 0
    b = 0
    c = 0
    candidatesChoices = ["a", "b", "c"]

    listSize = int(input("Digite quantos numeros voce quer colocar: "))

    for i in range(1, listSize+1):

        listElement = input("Digite seu voto: ")

        while listElement not in candidatesChoices:
            print("Voto invalido, deve ser entre a, b ou c")
            listElement = input("Digite seu voto: ")
        
        if listElement == "a":
            a += 1
            print("Voto confirmado")
        elif listElement == "b":
            b += 1
            print("Voto confirmado")
        else:
            c += 1
            print("Voto confirmado")

    print(f"O candidato a ganhou {a} votos")
    print(f"O candidato b ganhou {b} votos")
    print(f"O candidato c ganhou {c} votos")

main()
