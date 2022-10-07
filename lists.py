# A = [1.1, 2.2, 3.2]                              # Delimitador de lista
# B = ['a'] * 5                                    # Multiplicação de lista
# C = list(range(5, 20, 3))                        # Typecast de uma sequência
# D = [ x**2 for x in range(1, 20) if x % 3 == 0 ] # List Comprehension
# print(A)
# print(B)
# print(C)
# print(D)


# 1. Implemente um programa que define um  vetor de 6 posições, inicializado com
# zeros. Em seguida, faça um laço que atualize o vetor de forma dinâmica com os
# valores [2 4 6 8 10 12], utilizando acesso indexado e uma fórmula matemática para
# calcular os valores. Nenhum elemento do  vetor  deve deixar de ser  atualizado.
# Depois, mostre todo o vetor na tela;

# lista = [0] * 6
# calculo = 2

# for index in range(len(lista)):
#     lista[index] += calculo
#     calculo += 2 

# print(lista)


# 2. Implemente um programa que define um vetor vazio. Em seguida, faça um laço que
# adicione no vetor os valores [−1.5 −1 −0.5 0 0.5 1 1.5 2 2.5 3] de forma dinâmica,
# utilizando uma fórmula matemática para calcular os valores. Nenhum elemento do
# vetor deve deixar de ser inicializado. Depois, faça outro laço que mostre todo o vetor
# na tela;

# lista = []
# calculo = -1.5

# while len(lista) < 10:
#     lista.append(calculo)
#     calculo += 0.5

# for i in lista:
#     print(i)

 
# 3. Monte um programa que peça para o usuário digitar 10 números fracionários, os
# armazene em um vetor e em seguida mostre na tela:
# a. O índice e o conteúdo do elemento de menor valor;
# b. O índice e o conteúdo do elemento de maior valor;
# c. A diferença entre os elementos de maior e menor valor;

# numeros = 0
# lista = []
# while len(lista) < 10:
#     lista.append(float(input('digite um numero fracionario: ')))

# print(lista.index(min(lista)), min(lista))    
# print(lista.index(max(lista)), max(lista))
# print( max(lista) - min(lista) )  

# 4. Monte um programa que leia 10 números inteiros positivos e os armazene em um
# vetor. Mostre os números na ordem inversa a que foram digitados;

# numeros = 0
# lista = []
# while len(lista) < 10:
#     lista.append(int(input('digite um numero inteiro: ')))

# lista.reverse()
# print(lista)

# 5. Monte um programa que leia 10 números inteiros positivos e os armazene em um
# vetor. Crie um segundo vetor e o alimente com os valores em ordem inversa ao
# primeiro. Mostre ambos na tela, percorrendo do primeiro ao último elemento;

# numeros = 0
# lista = []

# while len(lista) < 10:
#     lista.append(int(input('digite um numero inteiro: ')))

# lista_dois = []

# for i in lista:
#     print(i)

# lista.reverse()

# for i in lista:
#     lista_dois.append(i)
#     print(i)


# 6. Monte um programa que leia 10 números inteiros positivos e os armazene em um
# vetor. Reorganize o próprio vetor armazenando seus elementos em ordem inversa.
# Não utilize outro vetor para isso, use apenas uma variável auxiliar. Mostre o vetor na
# tela após a inversão dos elementos;

# numeros = 0
# lista = []
# while len(lista) < 10:
#     lista.append(int(input('digite um numero inteiro: ')))

# for i in range(len(lista)):
#     last_item = lista.pop()
#     lista.insert(i, last_item)

# print(lista)


# 7. Alimente um vetor com 10 números e o imprima. Peça para o usuário informar um
# número   e   o   procure   no  vetor.   Se   encontrar,   imprima   o   número   lido   e   a(s)
# posição(ões) em que foi(foram) encontrado(s). Se não encontrar, imprima o número
# lido e a mensagem "NÃO ENCONTRADO";

# lista = []
# while len(lista) < 10:
#     lista.append(float(input('digite um numero: ')))

# numero = float(input('digite um valor da lista: '))
# if numero not in lista:
#     print ('NÃO ENCONTRADO')
# else:
#     for i in range(len(lista)):
#         if(numero == lista[i]):
#             print(i, lista[i]) 

# 8. Crie um programa que solicita  ao usuário digitar 5 números fracionários e os
# armazena em um vetor “A”. Depois, solicite mais 5 números e armazene em um
# segundo  vetor “B”. Mostre na tela as operações matemáticas soma, subtração,
# multiplicação e divisão, índice por índice dos vetores;

# A = []
# while len(A) < 5:
#     A.append(float(input('digite um numero: ')))

# B = []
# while len(B) < 5:
#     B.append(float(input('digite um numero: ')))

# for a, b in zip(A, B):
#     print("soma {}".format(a + b))
#     print("subtracao {}".format(a - b) )
#     print("multiplicacao {}".format(a * b))
#     print("divisao {}".format(a / b))


# 9. Desafio: Monte um programa onde o usuário entra com o valor das diversas notas
# alcançadas por uma turma de alunos. O programa inicia perguntando o tamanho da
# turma e parte para a entrada de dados. A seguir, o programa deve ser capaz de
# exibir um histograma na tela, além de outras informações, conforme é mostrado a
# seguir:
# Obs   1:   Ao   lado   da   menor   e   da   maior   nota,   deve   ser   mostrado   entre
# parênteses a quantidade de vezes que essa nota apareceu;
# Obs 2: Por exemplo, na linha "7.1~8.0" os 5 “*” significam que 5 alunos
# alcançaram uma nota > 7.0 mas <= 8.0.
# Resultado da avaliação da turma:
# Menor nota: 2.1 (1x)
# Maior nota: 10.0 (2x)
# Média da turma: 6.5
# Histograma das notas:
# 0.0 ~  3.0: ***
# 3.1 ~  4.0: **
# 4.1 ~  5.0: ****
# 5.1 ~  6.0: *******
# 6.1 ~  7.0: **********
# 7.1 ~  8.0: *****
# 8.1 ~  9.0: *
# 9.1 ~ 10.0: **

# tamanho = int(input("digite o tamanho da turma: "))
# lista = []

# while len(lista) < tamanho:
#     lista.append(float(input('digite uma nota do aluno: ')))

# nota_minima = min(lista)
# nota_maxima = max(lista)
# qtd_nota_minima = lista.count(nota_minima)
# qtd_nota_maxima = lista.count(nota_maxima)
# media = sum(lista) / len(lista)

# notas_zero_tres = len(list(filter(lambda x: x > 0 and x <= 3, lista)))
# notas_tres_quatro = len(list(filter(lambda x: x > 3 and x <= 4, lista)))
# notas_quatro_cinco = len(list(filter(lambda x: x > 4 and x <= 5, lista)))
# notas_cinco_seis = len(list(filter(lambda x: x > 5 and x <= 6, lista)))
# notas_seis_sete = len(list(filter(lambda x: x > 6 and x <= 7, lista)))
# notas_sete_oito = len(list(filter(lambda x: x > 7 and x <= 8, lista)))
# notas_oito_nove = len(list(filter(lambda x: x > 8 and x <= 9, lista)))
# notas_nove_dez = len(list(filter(lambda x: x > 9 and x <= 10, lista)))

# print("Resultado da avaliação da turma:")
# print("Menor nota: {} ({})".format(nota_minima, qtd_nota_minima)) 
# print("Maior nota: {} ({})".format(nota_maxima, qtd_nota_maxima)) 
# print("Média da turma: {}".format(media)) 
# print("Histograma das notas:")
# print(" 0.0 ~  3.0: {}".format("*" * notas_zero_tres))
# print(" 3.1 ~  4.0: {}".format("*" * notas_tres_quatro))
# print(" 4.1 ~  5.0: {}".format("*" * notas_quatro_cinco))
# print(" 5.1 ~  6.0: {}".format("*" * notas_cinco_seis))
# print(" 6.1 ~  7.0: {}".format("*" * notas_seis_sete))
# print(" 7.1 ~  8.0: {}".format("*" * notas_sete_oito))
# print(" 8.1 ~  9.0: {}".format("*" * notas_oito_nove))
# print(" 9.1 ~ 10.0: {}".format("*" * notas_nove_dez))