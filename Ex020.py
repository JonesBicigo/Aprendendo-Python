from random import sample
print('----Gere uma ordem de Apresentação----')
n1 = (input('Primeiro aluno:'))
n2 = (input('Segundo aluno:'))
n3 = (input('Terceiro aluno:'))
n4 = (input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
novalista = sample(lista, k=len(lista))
print('Essa será a ordem de apresentação dos trabalhos:{}.'.format(novalista))
