file = open('municipios.txt')
titulo = file.readline().strip()
f = file.readlines()
file.close()  

matriz = []
index_municipio = 0
index_populacao = 1
index_pib = 2

for linha in f:
    format = linha.replace("\n", "").replace("\t", ",").split(",")
    matriz.append(format)    

lista_municipios_sem_composto = []

for i in matriz:
    if not " " in i[index_municipio]:
        lista_municipios_sem_composto.append(i[index_municipio])
print("\n")
print("a) Municipios que não possuem nome composto")
for i in lista_municipios_sem_composto:
    print(i)

print("\n")
print("b) A população e o nome dos municípios que possuem menos que 22000 ou mais que 41000 habitantes")
for i in matriz:
    if int(i[index_populacao]) < 22000 or int(i[index_populacao]) > 41000:
        print(i[index_municipio] + " - " + i[index_populacao] + " habitantes")

print("\n")
print("c) O PIB e o nome dos municípios com PIB per capita entre R$40.000 e R$50.000.")
for i in matriz:
    calculo_pib = float(i[index_pib]) / int(i[index_populacao]) * 10 ** 6
    if calculo_pib >= 40000 and calculo_pib <= 50000 :
        print("Nome do municipio: {} e PIB: {:.2f}".format(i[index_municipio], calculo_pib))