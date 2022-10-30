import math
print('---Triângulo Retângulo---')
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento cateto adjacente:'))
hi = math.hypot (co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
