texto = None
lista = []

while texto != "":
    texto = input("digite a letra desejada: ")
    
    if texto == "":
        break

    if texto in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or texto in "abcdefghijklmnopqrstuvwxyz":
        if not texto in lista:
            lista.append(texto)    
    else: 
        print("letra informada é inválida")

for i in lista:
    print(i)