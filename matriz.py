# 1. Criar uma matriz de números fracionários com 10 linhas e 10 colunas. Inicializar cada 
# elemento da matriz com a parte inteira correspondente ao índice da linha e a parte 
# fracionária correspondente ao índice da coluna. Imprimir a matriz na tela mostrando os 
# números com precisão de uma casa decimal;

linhas = 10
colunas = 10
numero = 10
M = []  
for i in range(linhas):
  M.append([numero] * colunas)

for i in range(linhas):
    for j in range(colunas):
        numero += 0.2
        M[i][j] = "%.1f" % numero     

for l in M:
  print(l)

# 2. Na matriz criada no item 1, percorrer a diagonal principal de [0][0] até [9][9] e mostrar 
# os elementos na tela;

# aux = 0

# for i in range(linhas):
#     print(M[aux][aux])
#     aux += 1


# 3. Na matriz criada no item 1, percorrer a diagonal secundária de [0][9] até [9][0] e mostrar 
# os elementos na tela;

# increment = 0
# decrement = len(M) - 1

# for i in range(linhas):
#     print(M[increment][decrement])
#     increment += 1
#     decrement -= 1


# 4. Na matriz criada no item 1, percorrer as bordas e mostrar os elementos na tela, em 
# formato tabular;

# for i in range(linhas):
#     print(M[0][i], M[i][0], M[len(M) - 1][i], M[i][len(M) - 1])
 

# 5. Transpor a matriz criada no item 1, criando uma nova matriz e permutando as linhas 
# pelas colunas. A linha 1 para coluna 1, linha 2 para coluna 2, linha “n” para coluna “n”. 
# Imprimir a matriz transposta;

# 6. Solicitar que o usuário informe as dimensões de uma matriz, obrigatoriamente menor 
# que 10 x 10. Copiar as últimas linhas e colunas da matriz do item 1 para dentro dessa 
# nova matriz e exibir na tela;

# 7. Criar uma matriz de caracteres 10 x 10 e inicializar todos os elementos com “-”. Depois, 
# alterar  para  o  valor  “X”  os  elementos  das  duas  diagonais  utilizando  estruturas  de 
# repetição. Imprimir a matriz na tela;