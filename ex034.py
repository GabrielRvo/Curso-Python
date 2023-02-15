salario = int(input('Digite o salário a ser analisado: R$'))

aumento = (salario * 0.15) + salario
aumento1 = (salario * 0.10) + salario
if salario <= 1250:
    print(f'O seu salário foi reajustado de R${salario} para R${aumento:.2f} ')
else:
    print(f'O seu salário foi reajustado de R${salario} para R${aumento1:.2f}')


