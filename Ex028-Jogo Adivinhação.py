import random
from time import sleep
num = int(input('Digite um número qualquer de 0 a 5:'))
print('PROCESSANDO...')
sleep(3)
computador = random.randint(0, 5)
if num == computador:
    print('Parabéns, você acertou MISERAVI.Também pensei em {}'.format(computador))
else:
    print('Você ERROU,eu pensei em {} hahaha!!'.format(computador))
