num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

if num1 > num2:
    for i in range(num2+1, num1):
        print(i)
elif num1 < num2:
    for i in range(num1+1, num2):
        print(i)
else:
    print("Os numeros sao iguais")

print("A soma dos numeros e:", num1 + num2)
