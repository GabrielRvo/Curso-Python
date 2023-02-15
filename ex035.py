print('Digite 3 números e confira se eles formam um triângulo. ')
a = float(input('Digite um lado: '))
b = float(input('Digite outro lado: '))
c = float(input('Digite o último lado: '))

if a < b + c and b < c + a and c < a + b:
    print('Esses valores PODEM formar um triângulo.')
else:
    print('Um triângulo NÃO pode ser formado por esses valores.')
