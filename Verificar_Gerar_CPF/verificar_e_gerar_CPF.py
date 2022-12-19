import re
import sys
import random

def soma_nove_digitos(cpf_nove):
    i = 10
    soma = 0
    for digito in cpf_nove:
        if i >= 2:
            soma = (int(digito) * i) + soma
            i -= 1
    resto = (soma * 10) % 11
    resto = resto if resto <= 9 else 0
    return resto

def soma_dez_digitos(cpf_dez):
    i = 11
    soma = 0
    for digito in cpf_dez:
        if i >= 2:
            soma = (int(digito) * i) + soma
            i -= 1
    resto = (soma * 10) % 11
    resto = resto if resto <= 9 else 0
    return resto

def gerarCPF():
    nove_digitos = ''
    digitos_finais = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    digitos_finais += f"{soma_nove_digitos(nove_digitos)}"
    digitos_finais += f"{soma_dez_digitos(nove_digitos+f'{soma_nove_digitos(nove_digitos)}')}"
    todos_digitos = nove_digitos + digitos_finais
    print(todos_digitos)
    return todos_digitos

def validar_cpf(cpf):
    ultimo_dois_digitos = f'{soma_nove_digitos(cpf)}' + f'{soma_dez_digitos(cpf)}'
    eh_valido = cpf.endswith(ultimo_dois_digitos)
    return eh_valido

menu_cpf = input('[1] Gerar CPF | [2] Verificar se é válido: ')
if menu_cpf == '1':
    print("Gerando CPF...")
    cpf_gerado = gerarCPF()
    if validar_cpf(cpf_gerado):
        print(f'O CPF {cpf_gerado} já foi verificado e validado')
    else:
        print('CPF invalido')

elif menu_cpf == '2':
    cpf_digitado = input('Digite seu CPF: ')

    if cpf_digitado == cpf_digitado[0] * len(cpf_digitado):
        print('Você repetiu muitos caracteres')
        sys.exit()

    else:
        cpf_digitado = re.sub(r'[^0-9]', '', cpf_digitado)
        if validar_cpf(cpf_digitado):
            print('Verificado e validado')
        else:
            print('CPF invalido')
else:
    print('Digite um número correto')