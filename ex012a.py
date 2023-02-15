# Outra forma, mais simples

produto = float(input('Qual o valor do produto? '))
desconto = produto - (produto * 0.05)

print(f'O produto que custava R${produto}, na promoção com o desconto de 5% vai custar R${desconto:.2f}')
