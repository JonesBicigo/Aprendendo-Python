salario = float(input('Digite o salário atual do colaborador:R$'))
if salario > 1250:
    calculo = (salario * 10) / 100
    novo = salario + calculo
    print('O colaborador ganha {:.2f} R$ o que é acima de 1250 R$ e terá um aumento de 10 %, ou seja: {:.2f} R$'.format(salario, novo))
if salario <= 1250:
    calculo = (salario * 15) / 100
    novo = salario + calculo
    print('O colaborador ganha {:.2f} R$ o que é abaixo de 1250 R$ e terá um aumento de 15 %,ou seja: {:.2f} R$'.format(salario, novo))
