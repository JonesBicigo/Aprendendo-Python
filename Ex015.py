dias = int(input('Por quanto tempo o veículo foi utilizado?' ))
locação = dias * 60.00
km = float(input('Quantos quilômetros rodados?km' ))
km = km * 0.15
print('Serão cobrados {} R$ Pela localção.E {:.2f} R$ por quilômetro rodado.'.format(locação, km))
print('Sendo 60.00 R$ e 0.15 por km rodado')