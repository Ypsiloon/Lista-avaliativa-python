# Jogo da Velha
# Este é um jogo da velha para dois jogadores com um tabuleiro de tamanho variável.
# O tabuleiro é uma matriz quadrada representada como uma lista de listas.
# O jogo continua até que um jogador vença ou haja um empate.

def criar_tabuleiro(tamanho):
    """
    Cria um tabuleiro vazio com o tamanho especificado.

    Args:
        tamanho: O tamanho do tabuleiro (número de linhas e colunas).

    Retorna:
        lista: O tabuleiro vazio como uma lista de listas.
    """
    tabuleiro = [ [ '_' for i in range(tamanho)] for j in range(tamanho)]
    return tabuleiro

def jogada(jogador_vez):
    """
    Solicita a coordenada para a jogada do jogador e atualiza o tabuleiro.

    Args:
        jogador_vez: O jogador atual ('X' ou 'O').

    """
    while True:
        jogador = input("Digite a cordenada que deseja jogar [linha][coluna]: ")
        linha,coluna = [int(posicao) for posicao in jogador.split()]
        if linha >= tamanho+1 or coluna >= tamanho+1:
            print(f"Digite um valor menor do que {tamanho+1}!")
        elif jogo_da_velha[linha-1][coluna-1] != "_":
            print("Valor ja inserido!")
        else:
            jogo_da_velha[linha-1][coluna-1] = jogador_vez
            break
    
def desenhar_tabuleiro():
    """
    Desenha o tabuleiro na tela.
    
    """
    for i in jogo_da_velha:
        print(i)

def variar_jogador(count_jogada):
    """
    Alterna entre os jogadores 'X' e 'O' com base no número de jogadas.

    Args:
        count_jogada: O número de jogadas até agora.

    Retorna:
        str: O jogador atual ('X' ou 'O').
    """
    if count_jogada % 2 == 0:
        jogador_vez =  'O'
    else:
        jogador_vez = 'X'
    return jogador_vez

def ganhou():
    """
    Verifica se um jogador venceu o jogo.

    Retorna:
        bool: True se algum jogador vencer, False caso contrário.
    """
    for linha in jogo_da_velha:
        if all(item == linha[0] and item != "_" for item in linha):
            return True
    for coluna in range(tamanho):
        if all(jogo_da_velha[i][coluna] == jogo_da_velha[0][coluna] and jogo_da_velha[i][coluna] != "_" for i in range(tamanho)):
            return True
    if all(jogo_da_velha[i][i] == jogo_da_velha[0][0] and jogo_da_velha[i][i] != "_" for i in range(tamanho)):
        return True
    if all(jogo_da_velha[i][tamanho - 1 - i] == jogo_da_velha[0][tamanho - 1] and jogo_da_velha[i][tamanho - 1 - i] != "_" for i in range(tamanho)):
        return True
    return False

count_jogada = 0
tamanho = int(input("Digite o valor da dimensão que deseja jogar: "))
jogo_da_velha = criar_tabuleiro(tamanho)
desenhar_tabuleiro()
while True:
    count_jogada += 1
    jogador_vez = variar_jogador(count_jogada)
    jogada(jogador_vez)
    desenhar_tabuleiro()
    if ganhou():
        print(f"O jogador {jogador_vez} venceu!")
        break
