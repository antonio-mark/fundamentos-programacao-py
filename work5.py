# 1. Calculadora  básica:  Solicite  ao  usuário  um  número,  um  operador  e  em 
# seguida outro número, por exemplo: 1 + 1   2.3 * 2   5 – 2.7   9.3 / 2.4
# •Interprete a expressão e dê o resultado correto;
# •Cada operação matemática deve ser uma função que retorna o resultado 
# da operação para o chamador;
# •A impressão do resultado deve ser feita a partir do chamador;

numeroUm = float(input('Informe um número: '))
operador = str(input('Informe um operador: '))
numeroDois = float(input('Informe outro número: '))

def operacao (numeroUm, operador, numeroDois):
    if(operador == "+"):
        return soma(numeroUm, numeroDois)
    
    if(operador == "-"):
        return subtracao(numeroUm, numeroDois)

    if(operador == "*"):
        return multiplicacao(numeroUm, numeroDois)

    if(operador == "/"):
        return divisao(numeroUm, numeroDois)

def soma (numeroUm, numeroDois):
    return numeroUm + numeroDois

def subtracao (numeroUm, numeroDois):
    return numeroUm - numeroDois

def multiplicacao (numeroUm, numeroDois):
    return numeroUm * numeroDois

def divisao (numeroUm, numeroDois):
    return numeroUm / numeroDois

resultado = operacao(numeroUm, operador, numeroDois)
print(resultado)

# 2. Declare  uma  função  chamada  “ehPositivo”  que  recebe  um  número  como 
# parâmetro. Deverá retornar  True caso o parâmetro seja positivo ou zero e 
# retornar False caso o número seja negativo. Crie um programa que chama a 
# função e imprime o resultado a partir do chamador;


def ehPositivo (numero):
    ehPositivo = False

    if (numero >= 0):
        ehPositivo = True

    return ehPositivo

resultado = ehPositivo(-4)
print(resultado)

# 3. Faça um procedimento chamado “raizes”, que recebe 3 parâmetros e calcula 
# as raízes conforme a fórmula de Baskara. O procedimento deverá utilizar a 
# função “ehPositivo” para verificar se o delta da fórmula de Baskara é positivo, 
# e imprimir na tela as raízes calculadas ou informar que não existem raízes. 
# Para testar o procedimento, faça a leitura dos 3 parâmetros no “main” e em 
# seguida chame o procedimento passando os 3 parâmetros;

def main ():
    a = float(input('Informe o A: '))
    b = float(input('Informe o B: '))
    c = float(input('Informe o C: '))

    resultado =  raizes(a, b, c)
    return resultado

def raizes (a, b, c):
    delta = b ** 2 - 4 * a * c

    if ehPositivo(delta):
        x1 = (- b + pow(delta, 0.5)) / 2 * a
        x2 = (- b - pow(delta, 0.5)) / 2 * a
        return "x1: {} e x2: {}".format(x1, x2)
    else:
        return "não existem raízes"

print(main())

# 4. Faça  um  programa  que  solicite  ao  usuário  informar  uma  hora,  minuto  e 
# segundo no formato “hh:mm:ss”. Crie uma função chamada “horaParaFloat” 
# que recebe esses 3 parâmetros separadamente. Essa função deverá retornar 
# um  número  float  representando  as  horas,  minutos  e  segundos  como  um 
# número  fracionário.  Ex:  “01:15:30”  =  1,2583  ou  “13:20:15”  =  13,3375. 
# Imprima o número fracionário a partir do “main”; 

def main ():
    hora = int(input('Informe uma hora: '))
    minuto = int(input('Informe um minuto: '))
    segundo = int(input('Informe um segundo: '))

    resultado = float(horaParaFloat(hora, minuto, segundo))
    return round(resultado, 4)

def horaParaFloat(hora, minuto, segundo):
    segundosEmHora = segundo / 3600
    minutosEmHora = minuto / 60

    return segundosEmHora + minutosEmHora + hora

print(main())


# 5. Altere  o  programa  anterior  e  adicione  um  procedimento  chamado 
# “floatParaHora”,  que  recebe  como  parâmetro  um  número  fracionário  e 
# imprime na tela as horas, minutos e segundos correspondentes, no formato 
# “hh:mm:ss”;

def main ():
    numero = float(input('Informe um numero fracionario: '))

    return float_para_hora (numero)
     

def float_para_hora (numero):
    numero *= 3600

    minuto = numero / 60 
    segundo = numero % 60

    hora = minuto / 60
    minuto = minuto % 60

    return "{:0>2}:{:0>2}:{:0>2}".format( int(hora), int(minuto), int(segundo) )

print(main())

# 6. Desenvolva um programa que pergunte ao usuário quanto ele ganha por hora (opção 1 
# no menu) e o número de horas trabalhadas no mês (opção 2 no menu). Calcule e 
# mostre o detalhamento do seu contracheque no referido mês, conforme o seguinte 
# menu:
# •Salário bruto (opção 3);•Quanto pagou ao INSS (opção 4) (11%);•Quanto pagou ao sindicato (opção 5) (2%);•O salário líquido (opção 6);•Sair (opção 7);
# •Caso não tenha sido informado o valor recebido por hora ou a quantidade de horas 
# trabalhadas, deve gerar uma mensagem avisando que não há dados suficientes;
