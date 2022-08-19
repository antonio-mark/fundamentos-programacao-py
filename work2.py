number_one = float(input('Informe o primeiro número: '))
number_two = float(input('Informe o segundo número: '))

print("-" * 20)
print("Soma")
print(number_one + number_two)

print("-" * 20)
print("Subtracao")
print(number_one - number_two)

print("-" * 20)
print("Multiplicacao")
print(number_one * number_two)

print("-" * 20)
print("Divisao")
print(number_one / number_two)

print("-" * 20)
print("Divisao inteira")
print(number_one // number_two)

print("-" * 20)
print("Resto da divisao inteira")
print(number_one % number_two)

print("-" * 20)
print("Exponenciacao")
print(number_one ** number_two)

print("-" * 20)
print("Maior entre 2 numeros")
print(max(number_one, number_two))

print("-" * 20)
print("Menor entre 2 numeros")
print(min(number_one, number_two))

print("-" * 20)
if(number_one > number_two) :
    print(number_one)   
else : 
    print(number_two)    

print("-" * 20)
if(number_one < number_two) :
    print(number_one)
else :
    print(number_two)


print("2 " + "-" * 20)
Celsius = int(input("Informe um número inteiro: "))
Fahrenheit = Celsius * 1.8 + 32
print("Fahrenheit: {}".format(Fahrenheit))

print("3 " + "-" * 20)
Fahrenheit = int(input("Informe um número inteiro: "))
Celsius = (Fahrenheit - 32) / 1.8
print("Celsius: {}".format(Celsius))

print("4 " + "-" * 20)
velocidade_km = float(input("Informe uma velocidade em Km/h: "))
velocidade_ms = velocidade_km / 3.6
print("Velocidade em m/s: " + str(velocidade_ms))

print("5 " + "-" * 20)
calcado = float(input("Informe o preço do calçado: "))
percentual = float(input("Informe o percentual de desconto: "))
valorDesconto = (calcado * percentual) / 100
valorFinal = calcado - valorDesconto
print("Valor do desconto é {} e o valor final é {}".format(valorDesconto, valorFinal))

print("6 " + "-" * 20)
raio = float(input("Informe o raio de um círculo: "))
diametro = raio * 2
circunferencia = 2 * raio * 3.14
area = 3.14 * raio ** 2
print("Diametro é {}, circunferência é {} e area é {}".format(diametro, circunferencia, area))

print("7 " + "-" * 20)
altura = float(input("Informe a altura de um retângulo: "))
largura = float(input("Informe a largura de um retângulo: "))
perimetro = 2 * (largura + altura)
area = largura * altura
print("Perimetro é {} e area é {}".format(perimetro, area))

print("8 " + "-" * 20)
altura = float(input("Informe a altura de um retângulo: "))
base = float(input("Informe a base de um retângulo: "))
area = (base * altura) / 2
print("Area é {}".format(area))

print("9 " + "-" * 20)
x = float(input("Informe um número: "))
y = float(input("Informe outro número: "))
elevado = x ** y
print("primeiro número elevado ao segundo {}".format(elevado))

import math

print("10 " + "-" * 20)
catetoAdjacente = float(input("Informe o cateto adjacente: "))
catetoOposto = float(input("Informe o cateto oposto: "))
hipotenusa = math.sqrt(catetoAdjacente ** 2 + catetoOposto ** 2)
perimetro = catetoOposto + catetoAdjacente + hipotenusa
area = (catetoOposto * catetoAdjacente) / 2
seno = catetoOposto / hipotenusa
cosseno = catetoAdjacente / hipotenusa
tangente = catetoOposto / catetoAdjacente
print("hipotenusa: {}, perimetro: {}, area: {}, seno: {}, cosseno: {}, tangente: {}"
.format(hipotenusa, perimetro, area, seno, cosseno, tangente))