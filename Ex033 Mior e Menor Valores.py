a = int(input('Digite um valor:'))
b = int(input('Digite um segundo valor:'))
c = int(input('Digite um terceiro valor:'))
# verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O Menor número digitado foi {}'.format(menor))
print('O Maior número digitado foi {}'.format(maior))
