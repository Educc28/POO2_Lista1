def main():
    salarioInicial = float(input("Digite o salario incial: "))
    anoAtual = int(input("Digite o ano atual: "))
    salarioFinal = salarioInicial * 1.015
    ano = 1997
    i = 2
    while ano < anoAtual:
        ano += 1
        i += 1
        salarioFinal = salarioFinal + (salarioFinal * (2**i * 0.015))
    print(f"Seu salario final e: {salarioFinal}")

main()