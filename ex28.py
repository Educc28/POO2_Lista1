import statistics

def main():
    CDAmount = int(input("Digite quantos CD's voce tem: "))
    CDSize = []

    for i in range(1, CDAmount+1):
        listElement = int(input("Digite o valor de cada CD: "))
        CDSize.append(listElement)


    CDMean = statistics.mean(CDSize)
    CDCost = sum(CDSize)
    print(f"O valor total de sua colecao e {CDCost} e a media de valor dos seus CD's e {CDMean}")


main()
