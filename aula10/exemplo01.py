def calcula_bonus(v, s):
    b = v * 0.10
    s = s + b
    return b, s



# Início do Código
META =12000

venda = float(input('Informe a venda do vendedor: '))
salario = float(input('Informe o salário: '))

if venda >= META:
    # chama a função p/ bônus de 10%
    bonus, novo_salario = calcula_bonus(venda, salario)

    print(f'\nSeu bônus é de: R${bonus}')
    print(f'Seu novo sálario é: R${novo_salario}')

else:
    print('Sem bônus')
    print(f'Salário: R$ {salario}')
