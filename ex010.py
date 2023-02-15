carteira = float(input('Quanto você tem na carteira? '))
dolar = carteira / 5.17
euro = carteira / 5.08
yen = carteira / 0.035
print(f'Com R${carteira}, você pode comprar US${dolar:.2f}')
print(f'Com R${carteira}, você pode comprar €{euro:.2f}')
print(f'Com R${carteira}, você pode comprar ¥{yen:.2f}')