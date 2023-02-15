viagem = int(input('Qual a distância da sua viagem em km²? '))
passagem_longa = viagem * 0.45
passagem_curta = viagem * 0.50
if viagem <= 200:
    print(f'Sua viagem ficou no valor de R${passagem_curta:.2f}')
else:
    print(f'Sua viagem ficou no valor de R${passagem_longa:.2f}')