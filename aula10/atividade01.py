def calcula_peso(p):
    m = (p - KILO) * 4
    return m


KILO = 100

peso = float(input('Informe o peso em Kilo da pesca: '))


if peso > KILO:
    multa = calcula_peso(peso)
    
    
    print(f'Você pescou: {peso}kg')
    print(f'Você recebeu multa de: R${multa}')
    
   
else:
    print('Sem multa.')