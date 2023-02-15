km = float(input('Quanto km rodados? '))
dia = int(input('Quantos dias alugado? '))
valor = (km * 0.15) + (dia * 60)

print(f'O total a pagar é de R${valor:.2f}')