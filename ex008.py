m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
dam = m / 10
dm = m * 10
hm = m / 100
km = m / 1000

print(f'A distância de {m} metros corresponde a:\n'
      f'{km}km\n'
      f'{hm}hm\n'
      f'{dam}dam\n'
      f'{dm:.0f}dm\n'
      f'{cm:.0f}cm\n'
      f'{mm:.0f}mm\n')