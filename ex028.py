from random import randint
from time import sleep
cpu = randint(0,100)
print('---'*30)
print('Vou pensar em um número entre 0 e 100. Tente adivinhar...')
print('---'*30)
player = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(3)
if player == cpu:
    print('Essa foi a última vez que conseguiu isso!')
else:
    print('Mais sorte na próxima kkkkk')
    print(f'Eu pensei no número {cpu}')





