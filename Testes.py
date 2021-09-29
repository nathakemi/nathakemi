DADOS = [['A', ['1', '2'], ['3', '4'], ['3', '6']], ['C', ['2', '3']], ['B', ['4', '5']]]

i =0
ii = 1
reserva = input()
area = reserva[38:]
pessoas = reserva[20]
pessoas = int(pessoas)
while i < len(DADOS):
    if DADOS[i][0] == area:
        print('print dados:', DADOS[i][0])
        while ii < len(DADOS[i]):
            #diferenca = pessoas - cadeiras
            #print('esse maior é o numero de cadeiras nessa area:', Max_cadeiras)
            #print('essa é a diferença entre o numero de pessoas e cadeiras:', diferenca)
            DADOS[i][ii][-1] = int(DADOS[i][ii][-1])
            if DADOS[i][ii][1] == pessoas:
                print('Um grupo de ', pessoas, ' pessoas ocupou uma mesa de', pessoas, 'lugares na area', area, '.')
                break
            elif DADOS[i][ii][1] < pessoas:
                print('não há vagas')
                break
