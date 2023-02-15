larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * larg
tinta = area / 2
print(f'Sua parede tem a dimensão de {alt}x{larg} e a sua área é de {area}m²')
print(f'Para pintar essa parede, você vai precisar de {tinta}L de tinta')
