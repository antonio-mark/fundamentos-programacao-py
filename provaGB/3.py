linhas = 0
colunas = 0

while linhas == 0 and colunas == 0:
    linhas = int(input("digite um numero inteiro de 3 a 9: "))
    colunas = int(input("digite um numero inteiro de 3 a 9: "))
    if linhas not in range(3, 10) or colunas not in range(3, 10):
        linhas = 0
        colunas = 0 

M = []  
for i in range(linhas):
    M.append(["X"] * colunas) if i == 2 else M.append([" "] * colunas)


for i in M:
    print(i)