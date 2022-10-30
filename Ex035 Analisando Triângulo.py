print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
r1 = float(input('Informe o tamanho da primeira reta: cm'))
r2 = float(input('Informe o tamanho da segunda reta: cm'))
r3 = float(input('Informar o tamanho da terceira reta: cm'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
