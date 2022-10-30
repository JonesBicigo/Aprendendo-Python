from time import sleep
velocidade = float(input('Qual a velocidade registrada?km'))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print('REGISTRANDO...E CALCULANDO...')
    print('$' * 5)
    sleep(3)
    print('Sua velocidade foi de {} KM/H e você tera que pagar uma multa de {:.2f}R$'.format(velocidade, multa))
    print('Boa viagem e tome mais cuidado!!!!')
else:
    print('Parabéns pela sua condução à {}KM/H!! Uma boa viagem!'.format(velocidade))
#não precisava desse else aqui.isso é uma condição simples
