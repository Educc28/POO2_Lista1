def conta(divida_inicial):
    quant_parcelas = 1
    divida = -1
    juros = -1
    valor_parcelas = -1
    taxa_juros = -1
    
    print("Valor da divida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela")
    while quant_parcelas <= 12:
        if quant_parcelas == 1:
            taxa_juros = 0
        else:
            taxa_juros = (5 + 5*quant_parcelas/3)/100
        juros = divida_inicial * taxa_juros
        divida = divida_inicial + juros
        valor_parcelas = divida/quant_parcelas
        
        print(f"R$ {divida} - {juros} - {quant_parcelas} - R$ {valor_parcelas}")
        if quant_parcelas == 1:
            quant_parcelas = quant_parcelas*3
        else:
            quant_parcelas = quant_parcelas + 3



def main():
    divida_inicial = float(input("Digite o valor da divida inicial: "))

    conta(divida_inicial)

    
main()