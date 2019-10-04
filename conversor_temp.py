'''
print('-'*10, 'Conversor de Temperatura', '-'*10)
print('\nConverta as medidas das principais temperaturas automaticamente:'
      '\nCelsius (ºC), Fahrenheit (ºF) e Kelvin (K).\n')

def conversor_temp(medida, unidade, conversao):
    """Função que retorna a temperatura convertida"""
    if unidade == 'c' and conversao == 'k':
        temp = medida + 273
        print(f'{temp:.2f} K')
    elif unidade == 'c' and conversao == 'f':
        temp = (1.8*medida) + 32
        print(f'{temp:.2f} ºF')
    elif unidade == 'k' and conversao == 'c':
        temp = medida - 273
        print(f'{temp:.2f} ºC')
    elif unidade == 'k' and conversao == 'f':
        temp = 1.8 * (medida-273) + 32
        print(f'{temp:.2f} ºF')
    elif unidade == 'f' and conversao == 'c':
        temp = (medida-32) / 1.8
        print(f'{temp:.2f} ºC')
    elif unidade == 'f' and conversao == 'k':
        temp = (medida+459.67) * 5/9
        print(f'{temp:.2f} K')
    else:
        print('Opção inválida. Digite corretamente nos campos.')

    return temp

unidade = conversao = ' '
while unidade and conversao not in 'ckf':
    medida = float(input('Digite o número a ser convertido: '))
    unidade = str(input('Digite a unidade de medida da temperatura a ser convertida '
                        '[\033[31mC\033[m/\033[31mF\033[m/\033[31mK\033[m]: ')).strip().lower()
    conversao = str(input('Digite a unidade de medida para a qual você quer '
                          'converter a temperatura [C/F/K]: ')).strip().lower()
conversor_temp(medida, unidade, conversao)
'''
'''
def exibeMsg():
    print('-'*15, 'Conversor de Temperatura', '-'*15)
    print('\nConverta as medidas das temperaturas automaticamente:'
          '\nCelsius (ºC) e Fahrenheit (ºF)\n')
exibeMsg()

def conversor_temp(medida, unidade, conversao):
    """Função que retorna a temperatura convertida"""
    if unidade == 'c' and conversao == 'f':
        temp = (1.8*medida) + 32
        print(f'{temp:.2f} ºF')
    elif unidade == 'f' and conversao == 'c':
        temp = (medida-32) / 1.8
        print(f'{temp:.2f} ºC')
    else:
        print('Opção inválida. Digite corretamente nos campos.')

    return temp

unidade = conversao = ' '
while unidade and conversao not in 'ckf':
    medida = float(input('Digite o número a ser convertido: '))
    unidade = str(input('Digite a unidade de medida da temperatura a ser convertida '
                        '[C/F]: ')).strip().lower()
    conversao = str(input('Digite a unidade de medida para a qual você quer '
                          'converter a temperatura [C/F]: ')).strip().lower()
conversor_temp(medida, unidade, conversao)
'''
'''
#informe seu Nome: Aline Atsuta Braga
#informe seu RA: 1900724
#===============================

# Exercício 1 #

def par(x):
    return (x%2==0)

def par_impar(x):
    if par(x):
        return "par"
    else:
        return "ímpar"
avaliador = int(input("Entre com um nº para verificar se é par ou ímpar: "))
print(f"{avaliador} é {par_impar(avaliador)}.")

# Exercício 2 #

def exibeMsg():
    print('-'*15, 'Conversor de Temperatura', '-'*15)
    print('\nConverta as medidas das temperaturas automaticamente:'
          '\nCelsius (ºC) e Fahrenheit (ºF)\n')
exibeMsg()

def getConvertTo(temp, unid):
    unid = unid.lower()
    if unid == "c":
        temp = 9.0 / 5.0 * temp + 32
        return "%s ºF" % temp
    if unid == "f":
        temp = (temp - 32) / 9.0 * 5.0
        return "%s ºC" % temp


in_temp = int(input("Qual a temperatura? "))
in_unid = str(input("Qual a unidade de medida (f ou c): "))

print(getConvertTo(in_temp, in_unid))

# Exercício 3 #

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

numero_termos = int(input("Quantos termos você quer mostrar? "))

def valido(x):
    if numero_termos <= 0:
       print("Tente novamente com um valor válido. O valor precisa ser um número inteiro e positivo.")
    else:
       print("Sequência Fibonacci: ")
       for i in range(numero_termos):
           print(fibonacci(i))
valido(numero_termos)
'''

'''
cont = 0

for i in range(10):
    idade = int(input("Qual a sua idade: "))
    if idade > 18:
        cont = cont + 1
print(f"O número de pessoas com idade maior que 18 anos é: {cont}.")
'''

print("-*" * 12, "TABUADA DO 1 AO 10", "-*" * 12)
for c in range(1, 11):
    for k in range(1, 11):
        print(f"{c} x {k} = {c*k}")
