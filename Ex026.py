frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A primeira letra A aparece na posição:{}'.format(frase.find('A')+1))
print('A última vez que a letra A aparece é na posição:{}'.format(frase.rfind('A')+1))
