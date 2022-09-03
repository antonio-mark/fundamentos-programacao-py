print("1 " + "-" * 20)
n = int(input('Informe um número inteiro: '))

# Iterador
for x in range(n, n + 6):
 print(x)

# Contador
x = n
while x < n + 6:
 print(x)
 x += 1

print("2 " + "-" * 20)
n = int(input('Informe um número inteiro: '))

for x in range(n, n + 6):
  if x % 2 == 0:
    print(x)

x = n
while x < n + 6:
 if x % 2 == 0:
    print(x)
 x += 1

print("3 " + "-" * 20)
n = int(input('Informe um número inteiro: '))

for x in range(n, n + 6):
  if x % 2 != 0:
    print(x)

x = n
while x < n + 6:
 if x % 2 == 1:
    print(x)
 x += 1

print("4 " + "-" * 20)
n = int(input('Informe um número inteiro: '))
result = 1

for n in range(1, n + 1):
  result *= n
print(result)

result = 1

while n != 1:
 result *= n
 n -= 1
print(result)

print("5 " + "-" * 20)

n = int(input('Informe um número inteiro: '))
result = 1.5

for n in range(n):
  print(result)
  result += 0.5

print("6 " + "-" * 20)

n = int(input('Informe um número inteiro: '))
p = float(input('Informe um número: '))
i = float(input('Informe um número: '))

for n in range(n):
  print(round(i, 2))
  i += p

print("7 " + "-" * 20)

list = []
par = 0
impar = 0
soma = 0
media = 0
maior = float("inf")
menor = float("inf")


n = 1
while n != 0:
 n = int(input('Informe um número inteiro: '))
 if n == 0:
    break
 list.append(n)

for n in list :
  if n % 2 == 0:
    par += 1
  if n % 2 != 0:
    impar += 1
  soma += n
  
maior = max(list, key=int)  # max(int(number) for number in numbers)
menor = min(list, key=int)
media = soma / len(list)

print("\nquantidade de números digitados: {}".format(len(list)))
print("quantidade de pares: {}".format(par))
print("quantidade de ímpares: {}".format(impar))
print("soma destes números: {}".format(soma))
print("média aritmética: {}".format(media))
print("maior número: {}".format(maior))
print("menor número: {}".format(menor))


print("8 " + "-" * 20)

for x in range(5):
    x = '*'
    print (x, x, x, x, x)

print("9 " + "-" * 20)

y = ''
for x in range(5):
    y += '* '
    print (y)


print("10 " + "-" * 20)

# length = len(y)
y = '* * * * *'
for x in range(5):  
    print (y)
    y = y[:-2]
    # y = y[length::-1]
    # y = y.replace('*', ' ', 1)
    # y = y[length::-1]



