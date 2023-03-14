import statistics

def main():
    listSize = int(input("Digite quantos idades voce quer colocar: "))
    list1 = []

    for i in range(1, listSize+1):
        listElement = int(input("Digite um numero: "))
        list1.append(listElement)


    classAge = statistics.mean(list1)

    if classAge <= 25:
        print("A turma e jovem, media de idades: ", classAge)
    elif classAge >25 and classAge <= 60:
        print("A turma e adulta, media de idades: ", classAge)
    else:
        print("A turma e idosa, media de idades: ", classAge)


main()
