import statistics

def main():
    turmaAmount = int(input("Digite quantas turmas existem: "))
    turmaSize = []

    for i in range(1, turmaAmount+1):
        listElement = int(input("Digite a quantidade de alunos para cada turma, respectivamente: "))

        while listElement > 40:
            print("Uma turma nao pode ter mais que 40 alunos, tente novamente.")
            listElement = int(input("Digite a quantidade de alunos para cada turma, respectivamente: "))
        turmaSize.append(listElement)


    classMean = statistics.mean(turmaSize)
    print("A media de alunos e: ", classMean)


main()
