nome = str(input('Qual é o seu nome completo? ')).strip()
print('Analisando...')
print(f'Seu nome em maiúsculas é {nome.upper()} ')
print(f'Seu nome em minúsculas é {nome.lower()}')

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
