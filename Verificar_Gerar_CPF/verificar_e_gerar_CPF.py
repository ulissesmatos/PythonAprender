import re
import sys
import random

def calcular_ultimos_2_digitos(cpf_nove):
    #Gera o primeiro digito para formar os 10 digitos recebendo apenas 9 digitos
    i = 10
    soma = 0
    # Um for reverso que multiplica os valores de 0-9 do cpf por 10-2 respectivamente
    for digito in cpf_nove:
        if i >= 2:
            soma = (int(digito) * i) + soma
            i -= 1
    resto = (soma * 10) % 11
    resto = resto if resto <= 9 else 0
    #Gera o segundo digito para formar os 11 digitos de um CPF verdadeiro
    cpf_dez = cpf_nove + f'{resto}'
    i2 = 11
    soma2 = 0
    # Outro for reverso que multiplica os valores de 0-9 do cpf por 11-2 respectivamente
    for digito2 in cpf_dez:
        if i2 >= 2:
            soma2 = (int(digito2) * i2) + soma2
            i2 -= 1
    resto2 = (soma2 * 10) % 11
    resto2 = resto2 if resto2 <= 9 else 0
    cpf_onze = cpf_dez + f'{resto2}'
    return cpf_onze

def gerarCPF():
    nove_digitos = ''
    todos_digitos = ''
    # Usa randomização para gerar nove digitos
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    # Pega os nove digitos random e adiciona os ultimos 2 digitos chamando a função de calcular
    todos_digitos = calcular_ultimos_2_digitos(nove_digitos)
    print(todos_digitos)
    return todos_digitos

def validar_cpf(cpf):
    # Chama a função de calcular para gerar e depos verificar se os ultimos dois digitos são válidos
    cpf_calculado = f'{calcular_ultimos_2_digitos(cpf)}'
    dois_digito = ''
    i = 10
    for _ in cpf_calculado:
        if i <= 11:
            # A variável dois_digitos armazena apenas os dois ultimos digitos para realizar o check
            dois_digito = f'{cpf_calculado[i]}' + f'{dois_digito}'
            i+=1
    # Verifica a partir de 'dois_digitos' se é True com os numeros digitados ou gerados
    eh_valido = cpf.endswith(dois_digito)
    return eh_valido

# Menu com as opções de Gerar ou receber um CPF do usuario
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
    # Faz uma verificação simples se o CPF digitado repete muitos caracters (ex. 111.111.111-11)
    if cpf_digitado == cpf_digitado[0] * len(cpf_digitado):
        print('Você repetiu muitos caracteres')
        sys.exit()
    else:
        # Trata a entrada do usuario e remove quais quer caracteres diferente de números (ex. .,-)
        cpf_digitado = re.sub(r'[^0-9]', '', cpf_digitado)
        if validar_cpf(cpf_digitado):
            print('Verificado e validado')
        else:
            print('CPF invalido')
else:
    print('Digite um número correto')