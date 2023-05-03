# variaveis
escolha = '0'
custo_por_km = '0'
cidade_origem = None
cidade_destino = None
tres_cidades = []
cidades_escolha_quatro = []

# abre csv e cria matriz
file = open('dist.csv')
csv = file.readlines()
file.close()
 
matriz = []

for linha in csv:
    campos = linha.replace("\n", "").split(",")
    matriz.append(campos)

# funçoes de validação
def custo_por_km_is_valid_or_default(custo_por_km):
    if custo_por_km <= '0' or not custo_por_km.replace('.','',1).isdigit():
        print('O valor informado é inválido!')
        custo_por_km = '0'
    return custo_por_km

def custo_por_km_is_valid(custo_por_km):
    if custo_por_km == '0':
        print('\nNão foi informado o custo por km rodado!') 
        return False
    else: return True

def cidades_are_valid(cidade_origem, cidade_destino):
    if cidade_origem == cidade_destino or cidade_origem not in matriz[0] or cidade_destino not in matriz[0]:
        print("\nCidades não existem no cadastro ou são iguais! \nDigite novamente\n")
        cidade_destino = None
        cidade_origem = None
    return cidade_origem, cidade_destino

def tres_cidades_are_valid(cidades, tres_cidades):
    array_cidades = cidades.replace(", ", ",").split(",")
    for i, cidade in enumerate(array_cidades):
        if cidade not in matriz[0] or cidade in array_cidades[i+1:] or len(array_cidades) != 3:
            print("\nCidades não existem no cadastro, são iguais ou não foi informado 3 cidades!\n")
            return tres_cidades
    return array_cidades

# funçao para salvar no historico.csv
def salva_historico(historico):
    log = open('historico.csv', 'a')
    log.write('\n')
    for i in historico:
        log.write(i) if i == historico[-1] else log.write(i + ',')
    log.flush()
    log.close()

# funçao de calculo menu escolha 2
def calcula_distancia_custo_total(cidade_origem, cidade_destino, custo_por_km):
    posicao_cidade_origem = matriz[0].index(cidade_origem)
    posicao_cidade_destino = matriz[0].index(cidade_destino)
    valor_distancia_destino = matriz[posicao_cidade_origem + 1][posicao_cidade_destino]
    custo_total_trecho = int(valor_distancia_destino) * float(custo_por_km)
    return valor_distancia_destino, custo_total_trecho

def calcula_escolha_tres(tres_cidades):
    posicao_primeira_cidade = matriz[0].index(tres_cidades[0])
    posicao_segunda_cidade = matriz[0].index(tres_cidades[1])
    posicao_terceira_cidade = matriz[0].index(tres_cidades[2])

    valor_distancia_primeira_segunda = matriz[posicao_primeira_cidade + 1][posicao_segunda_cidade]
    valor_distancia_primeira_terceira = matriz[posicao_primeira_cidade + 1][posicao_terceira_cidade]
    valor_distancia_segunda_terceira = matriz[posicao_segunda_cidade + 1][posicao_terceira_cidade]
    valor_distancia_terceira_segunda = matriz[posicao_terceira_cidade + 1][posicao_segunda_cidade]

    if valor_distancia_primeira_segunda < valor_distancia_primeira_terceira:
        print("\nDe {} até {} são {} Km e de {} até {} são {} Km".format(tres_cidades[0].capitalize(), tres_cidades[1].capitalize(), 
                                                                        valor_distancia_primeira_segunda,
                                                                        tres_cidades[1].capitalize(), tres_cidades[2].capitalize(), 
                                                                        valor_distancia_segunda_terceira))
        print("\nDistância total percorrida: {} Km".format(int(valor_distancia_primeira_segunda) + int(valor_distancia_segunda_terceira))) 
    else:
        print("\nDe {} até {} são {} Km e de {} até {} são {} Km".format(tres_cidades[0].capitalize(), tres_cidades[2].capitalize(), 
                                                                        valor_distancia_primeira_terceira,
                                                                        tres_cidades[2].capitalize(), tres_cidades[1].capitalize(), 
                                                                        valor_distancia_terceira_segunda))
        print("\nDistância total percorrida: {} Km".format(int(valor_distancia_primeira_terceira) + int(valor_distancia_terceira_segunda)))   

# funçao de calculo menu escolha 4
def calcula_escolha_quatro(array_cidades):
    for cidade in array_cidades:
        posicao_cidade_origem = matriz[0].index(cidade_origem)
        posicao_cidade_destino = matriz[0].index(cidade_destino)
        valor_distancia_destino = matriz[posicao_cidade_origem + 1][posicao_cidade_destino]

# funçao escolha um
def escolha_um():
    custo_por_km = input("Informe o custo por km rodado: ")
    custo_por_km = custo_por_km_is_valid_or_default(custo_por_km)
    return custo_por_km

# funçao escolha dois
def escolha_dois(cidade_origem, cidade_destino, custo_por_km):
    while cidade_origem == None and cidade_destino == None:
        cidade_origem = input("Informe a cidade de origem: ").upper()
        cidade_destino = input("Informe a cidade de destino: ").upper()
        cidade_origem, cidade_destino = cidades_are_valid(cidade_origem, cidade_destino)
    
    valor_distancia_destino, custo_total_trecho = calcula_distancia_custo_total(cidade_origem, cidade_destino, custo_por_km)
    
    print("\nDistância rodoviária entre {} e {}: {} Km".format(cidade_origem.capitalize(), cidade_destino.capitalize(), valor_distancia_destino))
    print("Custo total do trecho: R$ {:.2f}".format(custo_total_trecho))

    historico = [cidade_origem, cidade_destino, valor_distancia_destino, custo_por_km, str(custo_total_trecho)]
    salva_historico(historico)

# funçao escolha tres
def escolha_tres(tres_cidades):
    cidades = input("Informe as três cidades: ").upper()
    tres_cidades = tres_cidades_are_valid(cidades, tres_cidades)
    if not tres_cidades:
        return   
    calcula_escolha_tres(tres_cidades)
      
# funçao escolha quatro
def escolha_quatro():
    cidade = ''
    while cidade.upper() != 'FIM':
        cidade = input("Informe no mínimo três cidades válidas (uma de cada vez) e digite \"fim\" quando terminar: ").upper()
        cidades_escolha_quatro.append(cidade)
    if len(cidades_escolha_quatro) < 3:
        print('Quantidade menor que 3, comando recusado')
        cidades_escolha_quatro.clear()
    for cidade in cidades_escolha_quatro:
        if cidade not in matriz[0]:
            print('Uma cidade informada é inválida')
            cidades_escolha_quatro.clear()
            escolha_quatro()
    calcula_escolha_quatro(cidades_escolha_quatro)
    
def menu():
    print('\n..:: Escolha sua opção ::..\n')
    print('1 - Custo por km rodado')
    print('2 - Consultar trecho')
    print('3 - Melhor rota')
    print('4 - Rota completa')
    print('5 - Sair\n')
    item = input('Escolha uma opção: ')
    return item      

while escolha != '5':
    escolha = menu()
    if escolha == '1':
        custo_por_km = escolha_um()
        
    elif escolha == '2':
        if custo_por_km_is_valid(custo_por_km): 
            escolha_dois(cidade_origem, cidade_destino, custo_por_km)

    elif escolha == '3':
        if custo_por_km_is_valid(custo_por_km): 
            escolha_tres(tres_cidades)

    elif escolha == '4':
        if custo_por_km_is_valid(custo_por_km): 
            escolha_quatro()

    elif escolha == '5':
        print('Sistema finalizado!') 
        break
        
    else:
        print('\nOpção desconhecida!\n')
        input('\n\nPressione ENTER para continuar   ')
        