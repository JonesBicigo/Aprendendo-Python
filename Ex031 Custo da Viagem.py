distancia = float(input('Qual foi a distância da viagem? km'))
passagemA = distancia * 0.50
passagemB = distancia * 0.45
if distancia <= 200:
    print('Sua viagem foi inferior à 200 KM,você rodou {} KM e pagará:{:.2f} R$'.format(distancia, passagemA))
else:
    print('Sua viagem foi acima de 200 KM,você viagou {} km totalizando {:.2f} R$'.format(distancia, passagemB))
print('****APROVEITE****')
