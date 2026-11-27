import random 
import subprocess



def soma(n, n2):
    r = n + n2
    return r

def subtracao(n, n2):
    r = n - n2
    return r

def multiplicacao(n, n2):
    r = n * n2
    return r

def divisao(n, n2):
    r = n / n2
    return r



# Início
subprocess.run('cls', shell=True)
numero_01 = float(input('\nDigite um número: '))
numero_02 = float(input('Digite outro número: '))

print('''
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
''')

opcao = int(input('Informe a opção: '))

match opcao:
    case 1:
        resultado = soma(numero_01, numero_02)

    case 2:
        resultado = subtracao(numero_01, numero_02)

    case 3:
        resultado = multiplicacao(numero_01, numero_02)

    case 4:
        resultado = divisao(numero_01, numero_02)

    case _:
        resultado = 'Opção inválida.'

print(f'Resultado: {resultado}')

    