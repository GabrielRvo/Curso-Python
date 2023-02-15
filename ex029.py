vel = int(input('Qual a velocidade do carro? '))
multa = (vel - 80)* 7
if vel >= 81:
    print('Este carro estava acima do limite de velocidade permitida.')
    print(f'Você foi multado em R${multa}.')
else:
    print('Seu carro estava dentro do limite permidito, siga sua viagem.')





