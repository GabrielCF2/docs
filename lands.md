~
# Lands
Sempre sonhou em ter a tão querida casa própria?

Pois agora seus problemas acabaram, com esses comando você pode se tornar o maior latifundiário do servidor, ou se menos
ambicioso apenas ter seu terreno com sua fazenda feliz!

quer saber quais são?

Arrasta para cima!

## comandos iniciais:
No servidor você pode requerir 1 (uma) ou mais chunks para si, sendo as 2 primeiras chuncks de graça (minha chunk minha vida) veja como:

### De inicio as contas
Você pode execurtar o comando entrando dento da chunk que deseja:

    /land create <nome>
_sendo \<nome> o nome da sua terra, nao precisando dos '<' e '>'_

Pronto agora você possui sua primeira chunk, a primeira e a segunda chunk é de graça, as seguintes obedecem à regra:

``preço da chunk atual =  valor da chunk anterior + 20%``

O preço de manutenção das chunks é dado pela função:

$\displaystyle 700 \left( 1 + 0.2 \right)^{c-1}$

c = quantidade de chunks

isto sendo cobrado de 15 em 15 dias

E mais uma cobraça é feita diariamente na função:

$\displaystyle 30x$

e x = quantidade de chunks so seu CPF.

## Comandos importantes:
Para adicionar uma nova chunk bas executar 

    /land claim
na chunk da sua preferência, sendo que a chunk seja consecutiva a sua land de inícial.

Cada player pode possuir 4 lands e cada uma com 75 chunks, para criar mais uma land fora a sua inicial basta não ser uma 
chunk que já possui dono e não consecutiva a lands já com donos.

Para confiar a sua terra a um player (ele poder contruir ou abrir baús na sua terra) use

    /land trust add <player> ` 
_sendo \<player> o nome do jogador que queira dar a permissão_

e

    /land

    /land delete confirm
Para apagar a land que você possui:

### Comandos para balance da land:
pode-se guardar dinheiro na terra usando:

    /land deposit <value>
_sendo \<value> o valor a ser descontado da sua conta e depositado na terra_

    /land balance
_mostra o balanço de dinheiro que possui na terra_

    /land withdraw <value>
_sendo \<value> o valor a ser retirado da land e ir para a sua carteira_

### Social da land
caso seja um grupo de playes integrantes da Land pode-se ter um canal de chat exclusivo para os mesmos

    /land chat <land> <message>
_sendo \<land> a land que deseja falar (caso tenha mais de 1) e \<message> a mensagem secreta
a ser transmitida_

## Comando de Nações
    /nations create <nome>
Cria uma nação onde \<nome> é o nome da nação.

    /nations accept
Comando para aceitar um convite recebido de se juntar a uma nação.

    /nations deny
Recusa um convite recebido para se juntar a uma nação.

    /nations delete
Comando para apagar uma nação e assim todos os amiguinhos estão cada um por si.

    /nations leave
Abandona os amiguinhos da nação preferindo seguir o caminho do lobo solitário.

    /nations rename <nome>
Onde \<nome> é o nome futoro assim alterando o nome da nação caso tenha ocorrido erros de digitação.

    /nations menu
Abre uma iterface para gerenciamento da nação e as lands participantes

    /nations setcapital \<capital>
Onde <capital> é a land a ser a futura capital da nação.

    /nations spawn
Teleporta para o Spawn da nação

    /nations relations
Abre a tela de relacionamento entre nações onde pose configurar estados de relacionamento entre nações

    /nations top
Mostra o Top 10 nações "evoluidas" do servidor, que tal tentar entrar nesse top?

## Guerras!
vamos esquentar as coisas tornandoa as coisas mais divertidas com carnificina!

    /wars declare <land>
Reclara guerram contra alguma land que vocês nao gostem, mas ela pose ser membro de uma nação respeitada, entao tome cuidado com suas
desavenças

    /wars info
Informações sobre como esta suas tropas e como as coisas estão fluindo

    /wars menu
Abre interface para verificar moso está o estado das guerras

    /wars spawn
Teleporta para a borda da land inimiga para voltar a linha de frente no campo de batalha!