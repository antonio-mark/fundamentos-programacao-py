print("1 " + "-" * 20)
x = input('Informe uma letra: ')
if x >= 'a' and x <= 'z':
    print('Letra minúscula')    
else:
    print('Letra maiúscula')

x = int(input('Informe um número: '))
if x < 10:
    print('Valor {} menor que 10'.format(x))
elif x > 10:
    print('Valor {} maior que 10'.format(x))
else:
    print('Valor {} igual a 10'.format(x))

print("2 " + "-" * 20)
n = int(input('Informe um número: '))

if n % 2 == 0 :
    print("é par")
else :
    print("é impar")

print("3 " + "-" * 20)
a = int(input('Informe um número: '))
b = int(input('Informe um número: '))

if a % b == 0:
    print("perfeitamente divisivel")
else:
    print("não é perfeitamente divisivel")

print("4 " + "-" * 20)
a = int(input('Informe um número: '))
b = int(input('Informe um número: '))

if a - b >= 0:
    print("resultado positivo")
else:
    print("resultado negativo")

print("5 " + "-" * 20)
numero = int(input('Informe um número: '))
inicialIntervalo = int(input('Informe um número inicial: '))
finalIntervalo = int(input('Informe um número final: '))

if numero >= inicialIntervalo and numero <= finalIntervalo :
    print("está dentro do intervalo")
elif numero > finalIntervalo :
    print("está acima do intervalo")
else :
    print("está abaixo do intervalo")

print("6 " + "-" * 20)
n = int(input('Informe uma temperatura em Celsius: '))

if n < 0 :
    print("sólido")
elif n >= 0 and n <= 100 :
    print("liquido")
else :
    print("gasoso")

print("7 " + "-" * 20)
a = str(input('Informe uma letra: '))
b = str(input('Informe uma letra: '))

if a > b :
    print("antecessor")
elif a == b :
    print("igual")
else :
    print("sucessor")

print("8 " + "-" * 20)
horaInicial = int(input('Informe uma hora: '))
minutoInicial = int(input('Informe um minuto: '))
segundoInicial = int(input('Informe um segundo: '))

horaFinal = int(input('Informe outra hora: '))
minutoFinal = int(input('Informe um minuto: '))
segundoFinal = int(input('Informe um segundo: '))

if horaFinal > horaInicial :
    resultadoHora = horaFinal - horaInicial
    resultadoMinuto = minutoFinal - minutoInicial
    resultadoSegundo = segundoFinal - segundoInicial
    resultado = '{:0>2d}:{:0>2d}:{:0>2d}'.format(resultadoHora, resultadoMinuto, resultadoSegundo)

elif horaFinal == horaInicial and minutoFinal > minutoInicial :
    resultadoHora = horaFinal - horaInicial
    resultadoMinuto = minutoFinal - minutoInicial
    resultadoSegundo = segundoFinal - segundoInicial
    resultado = '{:0>2d}:{:0>2d}:{:0>2d}'.format(resultadoHora, resultadoMinuto, resultadoSegundo)

elif horaFinal == horaInicial and minutoInicial > minutoFinal :
    resultadoHora = horaInicial - horaFinal
    resultadoMinuto = minutoInicial - minutoFinal
    resultadoSegundo = segundoInicial - segundoFinal
    resultado = '{:0>2d}:{:0>2d}:{:0>2d}'.format(resultadoHora, resultadoMinuto, resultadoSegundo)

else :
    resultadoHora = horaInicial - horaFinal
    resultadoMinuto = minutoInicial - minutoFinal
    resultadoSegundo = segundoInicial - segundoFinal
    resultado = '{:0>2d}:{:0>2d}:{:0>2d}'.format(resultadoHora, resultadoMinuto, resultadoSegundo)

print('{}'.format(resultado))


print("9 " + "-" * 20)
distancia = input('Informe a distancia: ')
velocidade = input('Informe a velocidade: ')
tempo = input('Informe o tempo: ')

if distancia == '' :
    distancia = float(velocidade) * float(tempo)
elif velocidade == '' :
    velocidade = float(distancia) / float(tempo)
else :
    tempo = float(distancia) / float(velocidade)

print('distancia: {} velocidade: {} tempo: {}'.format(distancia, velocidade, tempo))

import math

print("10 " + "-" * 20)
x1 = int(input('Informe a x1: '))
y1 = int(input('Informe a y1: '))
x2 = int(input('Informe o x2: '))
y2 = int(input('Informe o y2: '))

distancia = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )

print('resultado: {}'.format(distancia))


print("11 " + "-" * 20)
altura = float(input('Informe sua altura: '))
genero = str(input('Informe o seu genero: '))

if genero == 'M':
    resultado = 72.7 * altura - 58
else:
    resultado = 62.1 * altura - 44.7

print(resultado)

peso = float(input('Informe seu peso: '))

if peso >= resultado * 1.05 and peso <= resultado * 1.05:
    print('está na faixa ideal')
elif peso > resultado * 1.05:
    print('está acima do peso')
else :
    print('está abaixo do peso')
