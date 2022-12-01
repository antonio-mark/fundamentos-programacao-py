# Elabore   uma   função   chamada   ”classificar(texto)”,   que   recebe   um   texto
# como parâmetro e retorna sua classificação como “número inteiro”, “número fracionário”,
# “texto” ou “em branco”.  Para  testar a função,  elabore um programa  que abra  o arquivo
# anexo   “dados.txt”,   leia   linha   por   linha   do   arquivo,   identifique   o   conteúdo   de   cada   linha
# através da função “classificar(texto)” e salve linha por linha no arquivo “classificados.txt”,
# no formato “texto = classificação”. “texto” são os valores lidos do arquivo  “dados.txt”  e
# “classificação” são os valores retornados pela função “classificar(texto)”. 

file = open('dados.txt')
linhas = file.readlines()
file.close()  


def classificar(texto):
    filewrite = open('classificados.txt', 'a')
    filewrite.write('\n')

    if not texto.replace('.','',1).isdigit() and texto != "":
        filewrite.write(texto + " = " + "texto")
    
    elif texto.isdigit():
        filewrite.write(texto + " = " + "número inteiro")

    elif texto.replace('.','',1).isdigit():
        filewrite.write(texto + " = " + "número fracionário")

    else: 
        filewrite.write(texto + " = " + "em branco")
    
    filewrite.close()



for linha in linhas:
    format = linha.replace("\n", "")
    classificar(format)