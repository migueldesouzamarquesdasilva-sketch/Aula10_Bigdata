
def dobro(x):
    r = x * 2
    return r

def triplo(y):
    t = y * 3
    return t

def quadrado(p):
    q = p **2
    return q

valor = float(input('Digite um valor: '))

print('''
[2] - Dobro
[3] - Triplo
[4] - Quadrado
''')

opcao = int(input('Informe a opção: '))

match opcao:
    case 2:
        resultado = dobro(valor)
        #print(f'O dobro desse número é: {resultado} ')
        
    case 3:
        resultado = triplo(valor)
        #print(f'O triplo desse número é: {resultado} ')

    case 4:
        resultado = quadrado(valor)
        #print(f'O quadrado desse número é: {resultado}')

    case _:
        resultado = 'Opção inválida.'
        #print('Opção inválida.')

print(f'Resultado: {resultado}')

