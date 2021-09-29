entrada = str(input())
if entrada == '--CONFIGURACAO':
    while entrada == '--CONFIGURACAO':
        DADOS = []
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
            pessoas = reserva[20]
            area = reserva[38:]
            print('essas são as pessoas:', pessoas)
            print('essa é a área:', area)
            if pessoas == c: #TA ERRADO PQ PEGA O ULTIMO C BURRA
                cadeiras = pessoas
                print('Um grupo de ', pessoas, ' pessoas ocupou uma mesa de', cadeiras, 'lugares na area', area,'.')
                #cadeiras é maior ou igual a pessoas
                # um if aqui
            elif c < pessoas: #TA ERRADO PQ PEGA O ULTIMO C BURRA
                print('não tem lugar')

            else:
                print('Um grupo de ', pessoas, ' pessoas ocupou uma mesa de', c, 'lugares na area', area, '.')
