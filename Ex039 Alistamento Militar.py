from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento:'.title()))
idade = atual - nasc
print('quem nasceu em {} tem {} anos de idade em {}'.format(nasc, idade, atual).title())

if idade == 18:

    print('você deve se alistar imediatamente.'.title())
elif idade < 18:

    calculo = 18 - idade #calculando quanto falta para se alistar
    print('ainda faltam {} anos para o seu alistamento!'.format(calculo).title())

    ano = atual + calculo #calcula em que ano será o alistamento
    print('seu alistamento será em {}'.format(ano))

elif idade > 18:

    calculo = idade - 18 #calcula quanto passou do alistamento
    print('você já deveria ter se alistado há {} anos.'.format(calculo).title())

    ano = atual - calculo #calcula quando foi o ano de alistamento
    print('seu alistamento foi em {}'.format(ano).title())
