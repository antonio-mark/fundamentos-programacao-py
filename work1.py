# 1.
print("Antonio")

nome = input('Informe seu nome: ')
print('Olá {}'.format(nome))

# 2.
idade = 20
print(idade)

# 3.
altura = 1.784
print(format(altura, '.2f'))

# 4.
print('{:<7} {:<7} {:<7} {:<7}\n'.format(1, 10 , 100, 1000))
print('{:^7} {:^7} {:^7} {:^7}\n'.format(1, 10 , 100, 1000))
print('{:>7} {:>7} {:>7} {:>7}\n'.format(1, 10 , 100, 1000))

# formato_de_colunas = '{:{align}{height}} {:{align}{height}} {:{align}{height}} {:{align}{height}}'

# print(formato_de_colunas.format(1, 10 , 100, 1000, align='<', height='7'))
# print(formato_de_colunas.format(1, 10 , 100, 1000, align='^', height='7'))
# print(formato_de_colunas.format(1, 10 , 100, 1000, align='>', height='7'))

# 5.
dia = int(input('Informe o dia do seu nascimento: '))
print(dia)

# 6.
dia = int(input('Informe o dia do seu nascimento: '))
mes = int(input('Informe o mes do seu nascimento: '))
print(dia)
print(mes)

# 7.
from datetime import datetime

dia = int(input('Informe o dia do seu nascimento: '))
mes = int(input('Informe o mes do seu nascimento: '))
ano = int(input('Informe o ano do seu nascimento: '))

data = datetime(ano, mes, dia)
data_formatada = data.strftime('%d/%m/%Y')

print(data_formatada)

# 8.
numero_fracionario = float(input('Informe um número fracionário ex(1.5) : '))

print(int(numero_fracionario))

print("{:0.0f}".format(numero_fracionario))
# print(format(numero_fracionario, '.0f'))

print("{:.3f}".format(numero_fracionario))

# 9.
simbolo = str(input('Informe o símbolo da moeda ex($) : '))
valor = float(input('Informe um valor : '))

print("{} ${:.2f}".format(simbolo, valor))

print(f"{simbolo} ${valor:.2f}")

print(simbolo + " $" + format(valor, '.2f'))

print(f'{simbolo} ${format(valor, ".2f")}')