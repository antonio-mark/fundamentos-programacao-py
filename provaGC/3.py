#  Crie uma matriz “M” com dimensões definidas pelo usuário em tempo de
# execução, sendo que não pode ter menos que 5 ou mais que 10 linhas e colunas. Caso os
# dados informados estejam fora desse intervalo, peça novamente ao usuário até que sejam
# informados dados válidos. Inicialize a matriz pela fórmula: M[i][j] = i * 10 + j, onde “i” é o
# índice da linha e “j” é o índice da coluna. Em seguida, mostre na tela a matriz completa em
# formato tabular, e abaixo, também em formato tabular, os elementos das interseções das 4
# últimas linhas e 3 últimas colunas.
# Exemplo de matriz 8 x 6:

linhas = 0
colunas = 0
M = [] 

while linhas == 0 and colunas == 0:
    linhas = int(input("digite um numero inteiro de linhas de 5 a 10: "))
    colunas = int(input("digite um numero inteiro de colunas de 5 a 10: "))
    if linhas not in (5,6,7,8,9,10) or colunas not in (5,6,7,8,9,10):
        print("Dados inválidos, digite novamente!")
        linhas = 0
        colunas = 0 

for i in range(linhas):
  M.append([0] * colunas)

for i in range(linhas):
    for j in range(colunas):
        M[i][j] = i * 10 + j

for i in M:
  print(i)

print("\n\n\n")

intersecao = M[-4:]

for i in intersecao:
    print(i[-3:])