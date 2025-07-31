import re 
import sys
#Calculo do cpf
entrada = input('CPF [XXX.XXX.XXX-XX] ou somente numeros: ')
cpf_enviado = re.sub(r'[^0-9]',
                     '',
                     entrada)
#Metodo re para substuir qualquer carecter que não seja numero
entrada_e_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)
if entrada_e_sequencial:
    print('Você digitou dados repetidos.')
    sys.exit()

#Algoritmo precisa de 9 digitos
nove_digitos = cpf_enviado[:9]
#Multiplicação desses valores com um contador regressivo começando no 10
#Algoritmo vai somar o resultado de cada digito multiplicado
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

print(f"Primeiro dígito verificador: {primeiro_digito}")
print(f"Segundo dígito verificador: {segundo_digito}")

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é valido')
else:
    print('CPF é invalido')



