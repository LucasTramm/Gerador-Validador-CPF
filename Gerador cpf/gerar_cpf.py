import random


nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))
    #Gerar numeros aleatorios de 0 a 9 digitos

contator_regressivo_1 = 10
resultado_digito_1 = 0 
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contator_regressivo_1
    contator_regressivo_1 -= 1
#multiplicar o resultado por 10 e fazer a divisão do resto por 11
primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
#Calculo do 2 digito
dez_digitos = nove_digitos + str(primeiro_digito)

contator_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contator_regressivo_2
    contator_regressivo_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
cpf_formatado = f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}'

print(f'Seu CPF gerado é: {cpf_gerado} ou {cpf_formatado}')