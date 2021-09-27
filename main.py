entrada = str(input())
while True:

    if entrada == '--CONFIGURACAO':
        while True:
            AUX = input()
            if AUX == '--ATENDIMENTO':
                entrada = '--ATENDIMENTO'
                break
            else:
                a, m, c = AUX.split(' ')

    if entrada == '--ATENDIMENTO':
        while True:
            AUX2 = input()

            if AUX2 == -1:
                entrada = -1
                break

            elif AUX2 == 1:
                reserva = str(input())
                pessoas = reserva[12]
                area = reserva[-2]
                cadeiras = reserva[-20]

    if entrada == -1:
        print('Bom descanso!')
        break

