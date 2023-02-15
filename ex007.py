n1 = float(input('Digite a Nota de Python: '))
n2 = float(input('Digite a Nota de HTML e CSS: '))
media = (n1 + n2) / 2

print(f'A média das notas é de: {media}')

if media <= 6.9:
    print('Você esta de recuperação!')

else:
    print('Você foi aprovado!')



