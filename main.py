# função que le os dados, retorna index
def percore_area(vetor, area):
    i = 0
    ii = 0
    while i < len(vetor):
        if vetor[i][0] == area:
            ii = i
            break
        i += 1
    return ii


# função que le os dados e a area, e retorna o index do vetor_area com
# desejado numero de cadeiras
def percore_cadeira(vetor, area, cadeira):
    i = 0
    ii = 1
    cadeira = int(cadeira)
    indexa = percore_area(vetor, area)
    while i < len(vetor[indexa]):

        if vetor[indexa][i][-1] == cadeira:
            ii = i
            break
        i += 1
    return ii


# Altera a quantia de mesas em uma determinada area e cadeiras
# retorna um novo vetor para ser chamado, logo precisa fazer DADOS = modificar_configuracao(z, x, op, y, DADOS)
# COMANDO 4
def modificar_configuracao(z, x, op, y, vetor):
    indexa = percore_area(vetor, y)
    indexc = percore_cadeira(vetor, y, x)
    z = int(z)
    if op == 'add':
        vetor[indexa][indexc][0] += z
    elif op == 'rem':
        vetor[indexa][indexc][0] -= z

    return vetor


# FALTA A PARTE DO OCUPADO, DEPENDE DE FAZER O COMANDO 1 POR INTEIRO
# COMANDO 2
def ocupacao(vetor):
    i = 0
    while i < len(vetor):
        ii = 1
        soma_mesas = 0
        while ii < len(vetor[i]):
            soma_mesas += vetor[i][ii][0]
            ii += 1
        print(vetor[i][0], soma_mesas)
        i += 1

# retorna o indice da sublista da melhor mesa
# Exemplo = [area, [mesa1, cadeira1], [mesa2, cadeira2], [mesa3, cadeira3]
# Vai retornar o index 1, se a melhor mesa for a 1
# return (exemplo), (vetor da posição que foi retirada)
#                               usar para a desoculpação

# COMANDO 1
def ocupar_mesa(vetor, x, y):
    i = 1
    ii = 1
    x = int(x)
    diferenca = 100
    indexa = percore_area(vetor, y)
    while i < len(vetor[indexa]):
        if vetor[indexa][i][-1] == x:
            diferenca = 0
            ii = i
        elif ((vetor[indexa][i][-1] - x) < diferenca) and vetor[indexa][i][-1] > x:
            diferenca = vetor[indexa][i][-1] - x
            ii = i
        i += 1
    return [diferenca, ii]

tempo = 0
DADOS = []
entrada = str(input())
# Dados são organizados em uma lista e sublistas
# Exemplo: DADOS = [['sala', [1, 2], [3, 4], [3, 6]], ['quinta', [2, 3]], ['quarto', [4, 5]]]
# A sublista é cada Area possivel, sendo o nome seu o primeiro elemento
# Depois do elemento zero temos outra sublista com o tipo de configuração
# Estrutura DADOS = [[Nome, [mesa, cadeiras], [mesa, cadeiras]],...]

if entrada == '--CONFIGURACAO':
    while entrada == '--CONFIGURACAO':
        while True:
            AUX = input()
            if AUX == "--ATENDIMENTO":
                entrada = '--ATENDIMENTO'
                break
            else:
                a, m, c = AUX.split(' ')

            JA_ADICIONOU = False
            i = 0
            while i < len(DADOS):
                if a == DADOS[i][0]:
                    JA_ADICIONOU = True
                    break
                else:
                    JA_ADICIONOU = False
                i = i + 1

            if JA_ADICIONOU:
                DADOS[i] = DADOS[i] + [[m, c]]
            else:
                DADOS = DADOS + [[a, [m, c]]]
        print('essse é o dado:', DADOS)
        print('essa é a entrada:', entrada)

if entrada == '--ATENDIMENTO':
    while True:
        AUX2 = int(input())
        tempo += 1

        if AUX2 == -1:
            entrada = -1
            print('Restaurante fechado.')
            print('Balanco final de mesas:')
            for area in DADOS:
                print('essas são as mesas:', area)
            print('Bom descanso!')
            break

        elif AUX2 == 1:
            reserva = str(input())
            quantia_pessoas = reserva[20]
            area_desejada = reserva[38:]
            #FUNÇAO DANDO ERRO
            ocupar_mesa(DADOS, quantia_pessoas, area_desejada)
            print(f'Um grupo de {quantia_pesspas} pessoas ocupou uma mesa de {ocupar_mesa} lugares na area {area_desejada}')

        #elif AUX2 == 2:
            #ocupacao(DADOS)

        #elif AUX2 == 3:

        elif AUX2 == 4:
            add = input()
            if len(add) == 58:
                Y = add[-1]
                Z = add[22]
                X = add[-25]
                OP = 'adicionar'

            else:
                Y = add[-1]
                Z = add[20]
                X = add[-25]
                OP = 'retirar'

            modificar_configuracao(Z,X,OP,Y,DADOS)
