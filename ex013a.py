prod = float(input('Qual o valor do produto? '))
desconto = prod * (10/100)
valfd = prod - desconto
parce = prod * (8/100)
valfp = prod + parce

print(f'O produto que custa R${prod:.2f}, caso seja pago á vista tem um desconto de R${desconto:.2f} ficando um total de R${valfd:.2f}.')
print(f'Caso seja pago á prazo o produto terá um acréscimo de 8% (R${parce:.2f}) no valor total, ficando R${valfp:.2f}.')
