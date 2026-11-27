import random
import subprocess
from auxiliar.funcoes2 import dobro, triplo, quadrado


subprocess.run('cls', shell=True)
valor = random.randint(1, 200)
print(valor)

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

