# 1. A partir de uma frase digitada pelo usuário, mostre na tela a quantidade total de 
# letras e de palavras dessa frase

# palavra = input("digite uma palavra:" )
# print(len(palavra.replace(' ', '')))
# print(len(palavra.strip().split()))

# 2. Escreva uma função que recebe duas palavras e mostre na tela se ambas são iguais 
# ou se a primeira é anterior ou posterior a segunda, conforme a ordem alfabética


# palavra = input("digite uma palavra: ")
# palavra2 = input("digite uma palavra: ")

# def fun(palavra, palavra2):
#     index = 0
#     if palavra == palavra2:
#         print('All right.')
#     else:
#         while index < len(palavra) and index < len(palavra2):
#             letrapalavra1 = palavra[index]
#             letrapalavra2 = palavra2[index]
#             if letrapalavra1 < letrapalavra2:
#                 print(palavra)
#                 break
#             if letrapalavra1 > letrapalavra2:
#                 print(palavra2)
#                 break
#             index = index + 1

# fun(palavra, palavra2)

# 3. Escreva um método que recebe 3 textos (sujeito, verbo e predicado), monte uma 
# nova frase com esses 3 elementos (separados por espaço) e em seguida imprima a 
# frase. Use diversas formas para montar a string, como operador "+", format e "f"

# sujeito = input("digite uma palavra: ")
# verbo = input("digite uma palavra: ")
# predicado = input("digite uma palavra: ")


# print("{} {} {}".format(sujeito, verbo, predicado))

# 4. Peça para o usuário digitar uma frase. Em seguida, imprima a frase em letras 
# maiúsculas, minúsculas, somente primeira letra da frase maiúscula e por fim, 
# somente a primeira letra de cada palavra da frase maiúscula
# Atividades

# 5. Escreva uma função que retorna um booleano indicando se uma string é ou não um 
# palíndromo, ou seja, se o inverso da string é igual a ela. Escreva um programa para 
# testar a função.

# 6. Escreva uma função que recebe uma string e imprime uma tabela com o número de 
# ocorrências de cada caractere da string. Escreva um programa para testar a função.

# 7. Escreva uma função que recebe uma string e substitua cada segmento de dois ou 
# mais espaços por um só espaço. Retorne a string modificada.

# 8. Escreva uma função que recebe como parâmetro as strings "seg" e "txt", e verifique 
# se "seg" é um segmento de "txt". Escreva um programa que use essa função
# Atividades

# 9. Crie uma função que recebe como parâmetro um texto digitado pelo usuário. Avalie 
# o conteúdo desse texto e indique se representa um número inteiro, um número 
# fracionário ou um texto qualquer

# 10.Crie uma função chamada “str_to_int()” que recebe uma string qualquer como 
# parâmetro e retorna o valor inteiro correspondente. Caso a string não represente um 
# número inteiro válido, deve retornar zero. Não utilize “try / except”

# 11.Crie uma função chamada “str_to_float()” que recebe uma string qualquer como 
# parâmetro e retorna o valor fracionário correspondente. Caso a string não represente 
# um número fracionário válido, deve retornar zero. Não utilize “try / except”


# 12.Crie uma função que recebe como parâmetro um número inteiro entre 0 e 99 e 
# devolve uma string com o valor por extenso
