print('Digite 3 números para saber qual é, respectivamente, o menor e o maior entre eles. ')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite o último número: '))

# Verificando o menor

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O menor valor digitado foi {menor}.')

# Verificando o maior

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O maior valor digitado foi {maior}.')
