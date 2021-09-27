PyDiner Dash
Dêivis está querendo começar sua carreira como empreendedor. Ele pretende abrir seu primeiro restaurante na pandemia! Refletindo nas últimas vezes que Dêivis pediu sua ajuda, dessa vez ele decidiu pedir sua ajuda antes que tudo desse errado! Ajude Dêivis a construir, gerir e analisar as estatísticas da ocupação de um restaurante!

Objetivo
O objetivo deste projeto é que o aluno aprenda a desenvolver um programa na linguagem Python utilizando o conceito de variáveis, captura e escrita de informações na tela, condicionais, iteração, funções, listas e boas práticas de programação.

Entrada e Comandos
Os dados a serem fornecidos tem o formato abaixo:

--CONFIGURACAO
a m c
a m c
a m c
.
.
.
--ATENDIMENTO
comando
texto (existirá caso o comando exija)
comando
texto (existirá caso o comando exija)
comando
texto (existirá caso o comando exija)
comando
texto (existirá caso o comando exija)
.
.
.
-1
onde:

--CONFIGURACAO marca o início da seção de configuração do espaço do restaurante. A configuração ocorrerá até que comece a seção de atendimentos do restaurante.
a indica a área que existirá no restaurante. a é uma string, 1≤quantidade(a)≤10
m indica quantas mesas com uma quantidade específica de cadeiras existirão naquela área. m é um inteiro 1≤m≤100
c indica quantas cadeiras cada mesa daquela área terá. c é um inteiro 1≤c≤100
--ATENDIMENTO marca o início da seção de atendimentos do restaurante. Os atendimentos ocorrerão até que seja encontrado o input de comando -1.
comando indica qual comando de atendimento será executado naquele momento. comando é um inteiro tal que comando∈{1,2,3,4,−1}.
texto indica um texto que alguns comandos irão precisar para funcionarem corretamente.
-1 marca o fim do programa.
A seguir há uma descrição de cada comando e a entrada adicional de texto, caso este necessite de uma.


1. Colocar um grupo de pessoas em uma mesa (comando = 1)
O comando 1 consiste em alocar uma mesa na área indicada restaurante para um grupo de pessoas. Para isso, é necessária uma linha abaixo do comando com o texto no seguinte formato:

Quero uma mesa para X pessoas na area Y
onde X indica quantas pessoas tem no grupo e Y indica qual a área o grupo quer ocupar.


***Particularidades do Comando***
Assuma que não serão requeridas mesas em áreas que não existem.

Além da implementação simples acima, o comando possui algumas particularidades tanto na entrada quanto no comportamento dos grupos que estão ocupando as mesas, que serão explicadas a seguir:

Organização otimizada
Como dito acima, você deve sempre alocar a menor mesa possível que ainda acomode um grupo de pessoas, para otimizar o uso dos lugares disponíveis no restaurante.


Permanência dos grupos
Como um restaurante é rotativo, ou seja, as pessoas tem que sair do restaurante para que outras entrem, cada grupo de pessoas ficará por um número finito de comandos, determinado pela equação
tempo_de_permanencia=quantidade(comandos)=(2∗X)+2

onde X é a quantidade de pessoas no grupo, e comandos são os comandos executados pelo usuário no input (incluindo este que está sendo explicado). Cada comando é uma unidade de tempo de permanência, ou seja, um casal que consiga uma mesa no restaurante permanecerá nele por até 6 comandos, ou seja, 6 unidades de tempo. É claro que, quando o restaurante fecha, não haverá mais comandos (mas os clientes poderão terminar suas refeições tranquilamente). O próprio comando de alocar uma mesa no restaurante para um grupo de pessoas também contará para o tempo de permanência.



2. Consulta de mesas (comando = 2)
Imprime como saída uma lista com cada área, em ordem alfabética, com o respectivo número de mesas ocupadas de um total de mesas.



3. Consulta de lotação (comando = 3)
Imprime como saída uma lista com cada área, em ordem alfabética, com a respectiva lotação atual e capacidade total.



4. Adição ou remoção de mesas (comando = 4)
O comando 4 consiste em adicionar ou remover mesas com quantidade específica de cadeiras em uma área. Para isso, é necessária uma linha abaixo do comando com o texto no seguinte formato:

Quero OP mais Z mesas com X cadeiras cada na area Y
onde OP ∈{adicionar,remover}, Z é a quantidade de mesas a serem adicionadas, X é a quantidade de cadeiras de cada mesa, e Y é a área em que as mesas serão adicionadas/removidas.

***Particularidades do comando***
Assuma que nunca serão adicionadas mesas em áreas não existentes, nem que serão removidas mesas que estão ocupadas ou que não existem!!!!!!!



5. Fechar restaurante e consulta da configuração final do restaurante (comando = -1)
Neste comando, é necessário imprimir a configuração final do restaurante, após a adição e remoção de mesas (caso tenham ocorrido), separadas por área (ordenadas em ordem alfabética), com a configuração de mesas e cadeiras (ordenadas em ordem crescente de cadeiras), e a quantidade de pessoas que entraram no restaurante.




Saída
Como dito acima, na seção de atendimentos, serão executados comandos para o restaurante. A seguir há uma descrição da saída desejada baseada em cada comando inserido. 

1. Colocar um grupo de pessoas em uma mesa (comando = 1)
Caso haja uma mesa com lugares o suficiente para acomodar a quantidade de pessoas, deve imprimir:
Um grupo de X pessoas ocupou uma mesa de L lugares na area Y.
onde L é a menor quantidade de lugares que uma mesa possui no espaço Y, que também pode acomodar um grupo de X pessoas;

Caso não tenha uma mesa com lugares o suficiente para acomodar a quantidade de pessoas (seja pela lotação ou por não ter nenhuma mesa grande o suficiente para o grupo de pessoas), deve imprimir: 
Nao foi possivel levar o grupo de clientes para uma mesa.

2. Consulta de mesas (comando = 2)
Imprime como saída uma lista com cada área, em ordem alfabética, com o respectivo número de mesas ocupadas de um total de mesas, no seguinte formato:

A1: (M1 de T1 mesas)
A2: (M2 de T2 mesas)
A3: (M3 de T3 mesas)
.
.
.
An: (Mn de Tn mesas)
onde A é a área existente, M é a quantidade de mesas ocupadas na área e T é a quantidade de mesas totais da área.





3. Consulta de lotação (comando = 3)
Imprime como saída uma lista com cada área, em ordem alfabética, com a respectiva lotação atual e capacidade total, no seguinte formato:

A1: (C1 de T1 pessoas)
A2: (C2 de T2 pessoas)
A3: (C3 de T3 pessoas)
.
.
.
An: (Cn de Tn pessoas)
onde A é a área existente, C é a quantidade de cadeiras ocupadas na área e T é a quantidade de cadeiras totais da área.





4. Adição ou remoção de mesas (comando = 4)
Imprima na tela a mensagem de confirmação:

Z mesas de X cadeiras OP com sucesso na area Y.
onde OP ∈{adicionadas,removidas}, Z é a quantidade de mesas a serem adicionadas, X é a quantidade de cadeiras de cada mesa, e Y é a área em que as mesas foram adicionadas/removidas.




5. Fechar restaurante e consulta da configuração final do restaurante (comando = -1)
É necessário imprimir a configuração final do restaurante, após a adição e remoção de mesas (caso tenham ocorrido), separadas por área (ordenadas em ordem alfabética), com a configuração de mesas e cadeiras (ordenadas em ordem crescente de cadeiras), e a quantidade de pessoas que entraram no restaurante, com o seguinte formato:

Restaurante fechado.
Balanco final de mesas:
A1:
 M1 mesas de C1 cadeiras.
 M2 mesas de C2 cadeiras.
 M3 mesas de C3 cadeiras.
A2:
 M4 mesas de C4 cadeiras.
 M5 mesas de C5 cadeiras.
.
.
.
Um total de T pessoas visitaram o restaurante hoje.
Bom descanso!
onde A são as áreas, M são quantas mesas de uma quantidade específica de cadeiras a área tem, C são quantas cadeiras cada mesa tem e T são quantas pessoas visitaram o restaurante.
