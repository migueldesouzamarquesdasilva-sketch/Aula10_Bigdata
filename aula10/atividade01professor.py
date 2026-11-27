def calcula_multa(e):
    m = e * MULTA
    return m
    


MULTA = 4
LIMITE = 100

peso = float(input('Informe o peso: '))

if peso > LIMITE:
    excedente = peso - LIMITE
    multa = calcula_multa(excedente)

    print(f'Você ultrapassou em {excedente} Kilos. \nO valor da Multa é R$ {multa}')

else:
    print('Não há multa')