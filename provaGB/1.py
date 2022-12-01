texto = input("digite o texto desejado: ")

def separa_palavras(texto):
    texto_formatado = ""
    for i in texto:
       if i.isupper():
           texto_formatado += " " + i       
       else: 
           texto_formatado += i 
    
    return texto_formatado.strip()

texto_formatado = separa_palavras(texto)
print(texto_formatado)