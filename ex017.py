oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
from math import hypot
hipotenusa = hypot(oposto,adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')