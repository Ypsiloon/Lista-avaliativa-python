# Lista-avaliativa-python
Aluno Felipe Franco Pinheiro

## ex1.py

1) Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3.

Este código é uma implementação simples do jogo da velha em Python. Ele permite que dois jogadores joguem alternadamente em um tabuleiro 4x4, verificando se alguém venceu com base nas regras padrão do jogo da velha. O código mantém um loop até que um jogador vença ou o jogo termine em empate.

#### Estratégia:
-------------------
- O tabuleiro é representado como uma lista com listas para que tenha o tamanho de 4x4.
- Os jogadores são representados pelos caracteres 'O' e 'X' e jogam alternadamente.
- Verifica todas as combinações possíveis de vitória (linhas, colunas e diagonais).

#### Detalhamento das estruturas usadas:
-------------------
- Lista Multidimensional `(jogo_da_velha)`: Uma lista multidimensional é usada para representar o tabuleiro do jogo. Cada elemento da lista é uma lista de quatro elementos, representando as quatro colunas do tabuleiro. O caractere '_' representa uma célula vazia, 'X' representa uma jogada do jogador X e 'O' representa uma jogada do jogador O.
- Laço de Repetição `(while True)`: Um laço de repetição infinito é usado para permitir que os jogadores façam jogadas até que o jogo termine.
- Função `jogada(jogador_vez)`: Uma função chamada jogada é criada para permitir que os jogadores façam suas jogadas. Ela recebe como parâmetro o jogador que está na vez e solicita as coordenadas da jogada ao jogador.
- Função `desenhar_tabuleiro()`: A função desenhar_tabuleiro é responsável por exibir o tabuleiro atual na tela.
- Função `variar_jogador(i)`: A função variar_jogador determina qual jogador deve fazer a próxima jogada com base no número de jogadas já realizadas.
- Função `ganhou()`: A função ganhou verifica se algum jogador venceu o jogo, verificando todas as combinações possíveis de vitória (linhas, colunas e diagonais).
- Condições de Controle de Fluxo `(if, elif, else)`: Condições de controle de fluxo são usadas para verificar as jogadas dos jogadores, detectar vitórias, empates e atualizar o estado do jogo.
- Variáveis `(i, jogador_vez)`:  Variáveis são usadas para controlar o número de jogadas, alternar entre os jogadores e armazenar o resultado do jogo.


## ex2.py

2) Crie um jogo da velha NxN em que o usuário deve definir as dimensões do tabuleiro (sempre quadrado).

Jogo da Velha em Python: Este código Python implementa o clássico Jogo da Velha. Os jogadores alternam entre 'X' e 'O' para preencher um tabuleiro de tamanho personalizável. O jogo verifica automaticamente as vitórias por linha, coluna ou diagonal e exibe o vencedor.

#### Estratégia:
-------------------
- O tabuleiro é representado como uma lista com listas para que tenha o tamanho de NxN decidido pelo proprio jogador.
- Os jogadores são representados pelos caracteres 'O' e 'X' e jogam alternadamente.
- Verifica todas as combinações possíveis de vitória (linhas, colunas e diagonais).

#### Detalhamento das estruturas usadas:
-------------------
- Função `criar_tabuleiro(tamanho)`: Esta função cria um tabuleiro vazio para o Jogo da Velha, representado como uma lista de listas, o tamanho do tabuleiro é especificado como um parâmetro. Cada elemento do tabuleiro é inicializado com o caractere '_', representando uma célula vazia.
- Função `jogada(jogador_vez)`: Uma função chamada jogada é criada para permitir que os jogadores façam suas jogadas. Ela recebe como parâmetro o jogador que está na vez e solicita as coordenadas da jogada ao jogador.
- Função `desenhar_tabuleiro()`: A função desenhar_tabuleiro é responsável por exibir o tabuleiro atual na tela.
- Função `variar_jogador(count_jogada)`: A função variar_jogador determina qual jogador deve fazer a próxima jogada com base no número de jogadas já realizadas.
- Função `ganhou()`: A função ganhou verifica se algum jogador venceu o jogo, verificando todas as combinações possíveis de vitória (linhas, colunas e diagonais).
- Condições de Controle de Fluxo `(if, elif, else)`: Condições de controle de fluxo são usadas para verificar as jogadas dos jogadores, detectar vitórias, empates e atualizar o estado do jogo.
- Variáveis `count_jogada e tamanho`:  Variáveis são usadas para controlar o número de jogadas. Armazena o tamanho do tabuleiro, definido pelo jogador. Respectivamente
- Lista `jogo_da_velha`: Representa o estado atual do tabuleiro do Jogo da Velha como uma lista de listas. As células vazias são representadas pelo caractere '_', e as células ocupadas por jogadores ('X' ou 'O') são atualizadas conforme as jogadas.


## ex3.py

3) Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve ser jogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras que já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à formatação.


Este código Python implementa um jogo de adivinhação de palavras, onde o jogador deve adivinhar uma palavra sorteada com base na quantidade de letras desejada. O jogador tem um número limitado de chances (vida) para acertar a palavra. O programa fornece dicas de cores para as letras da palavra, indicando letras corretas no lugar correto (verde), letras corretas no lugar errado (amarelo) e letras erradas (cinza). O jogador também recebe feedback sobre as letras já usadas e o estado do teclado disponível. O jogo continua até o jogador vencer ou perder.

#### Estratégia:
-------------------
- O programa escolhe aleatoriamente uma palavra de um documento txt com base no tamanho especificado pelo usuario.
- O usuario faz tentativas até acabar suas vidas(6) ou adivinhar a palavra escolhida.
- O programa fornece dicas de maneira visual sobre as palavras utilizadas pelo usuario, destacando letras corretas no lugar certo(verde), letras corretas no lugar errado(amarelo) e letras erradas(cinza).

#### Detalhamento das estruturas usadas:
-------------------
- Lista `lista`: Armazena uma lista de palavras lidas de um arquivo de texto
- Função `escolher_palavra()`: Seleciona uma palavra aleatória com base na quantidade de letras desejada pelo jogador. Utiliza a lista de palavras disponíveis e escolhe uma palavra com o tamanho correto.
- Função `inicia_letras(palavra)`: Inicializa uma lista de caracteres '_' para representar as letras da palavra ocultas. Retorna uma lista com o mesmo número de '_' que a palavra sorteada.
- Função `verificar_palavra(palavra, chute)`: Compara a palavra sorteada com a tentativa do jogador (chute). Gera uma dica (lista de cores) para cada letra da palavra com base na correspondência.
- Função `colorir_palavra(palavra, dica)`: Cria uma representação colorida da palavra oculta com base na dica gerada. Utiliza códigos de escape ANSI para colorir o texto no terminal.
- Função letras_usadas`(teclado, palavra_sorteada, chute)`: Atualiza a lista de letras disponíveis (teclado) após cada chute do jogador. Remove letras usadas da lista para evitar chutes repetidos.
- Variáveis e Estruturas de Controle:
`letras_corretas`: Conjunto para armazenar letras corretas já adivinhadas.
`vida`: Número de vidas do jogador.
`perdeu e ganhou`: Variáveis de controle para determinar o resultado do jogo.
`historico`: Lista que mantém um registro dos chutes anteriores.
`teclado`: Lista que representa as letras disponíveis para chutar.


## ex4.py

4) “Banco de dados” de dicionários.

Este código Python permite o cadastro e gerenciamento de usuários, com campos obrigatórios e opcionais. Ele oferece funcionalidades como cadastrar usuários, imprimir todos os usuários ou filtrá-los com base em nomes e campos específicos. Utiliza estruturas de controle e entrada de dados para interação com o usuário.

#### Estratégia:
-------------------
- O código permite o cadastro de usuários com campos obrigatórios e opcionais. Os campos são armazenados em um dicionário chamado dados_usuario.
- O código permite a adição de campos adicionais opcionalmente. Isso é feito através do uso de uma condição que verifica se o usuário deseja continuar ou sair.
- Oferece opções para imprimir todos os usuários, filtrar por nomes, filtrar por campos específicos ou combinar filtros de nome e campos. Isso é alcançado usando a estrutura match para lidar com diferentes opções.

#### Detalhamento das estruturas usadas:
-------------------
- Dicionários: O código faz uso extensivo de dicionários Python para armazenar informações dos usuários. Cada usuário é representado como um dicionário, onde as chaves são por exemplo os campos (como "nome", "email", etc.) e os valores são os dados inseridos pelo usuário.
- Laços de Repetição: Laços de repetição, como `for` e `while`, são usados para iterar pelos campos obrigatórios e campos adicionais inseridos pelo usuário. Eles permitem coletar informações e verificar se o usuário deseja inserir campos adicionais.
- Listas e Split: Listas são usadas para armazenar campos obrigatórios e nomes de usuários. Além disso, a função `split()` é empregada para dividir as entradas do usuário em listas, por exemplo, ao separar os nomes de usuários inseridos com vírgulas.
- Match (Correspondência de Padrões): O código utiliza a estrutura `match` para direcionar o programa com base na escolha do usuário. Dependendo da opção escolhida, diferentes blocos de código são executados, permitindo operações como cadastro de usuário, impressão de todos os usuários ou filtragem com base em critérios específicos.
- Função `cadastrar_usuario(campos_obrigatorios)`: Esta função recebe uma lista de campos obrigatórios como argumento. Itera pelos campos obrigatórios e pede ao usuário para inserir dados para cada um. Permite ao usuário adicionar campos adicionais de forma opcional. Retorna um dicionário contendo os dados do usuário.
- Função `imprimir_usuarios(opcao)`: Recebe uma opção como argumento para determinar qual operação realizar. Dependendo da opção escolhida, esta função pode imprimir todos os usuários, filtrar por nomes, campos ou combinações de ambos. A função utiliza a estrutura match para direcionar o comportamento com base na opção.
