jogo_da_velha = [
                ['_','_','_','_'],
                ['_','_','_','_'],
                ['_','_','_','_'],
                ['_','_','_','_'] ]

def jogada(jogador_vez):
    while True:
        jogador = input("Digite a cordenada que deseja jogar [linha][coluna]: ")
        linha,coluna = [int(posicao) for posicao in jogador.split()]
        if linha >= 5 or coluna >= 5:
            print("Digite um valor menor do que 5!")
        elif jogo_da_velha[linha-1][coluna-1] != "_":
            print("Valor ja inserido!")
        else:
            jogo_da_velha[linha-1][coluna-1] = jogador_vez
            break
    
def desenhar_tabuleiro():
    for i in jogo_da_velha:
        print(i)

def variar_jogador(i):
    if i % 2 == 0:
        jogador_vez =  'O'
    else:
        jogador_vez = 'X'
        #print('\033[1;33;0m Olá, Mundo\033[m')
    return jogador_vez

def ganhou():
    for linha in jogo_da_velha:
        if linha[0] == linha[1] == linha[2] == linha[3] != "_":
            return True
    for coluna in range(4):
        if jogo_da_velha[0][coluna] == jogo_da_velha[1][coluna] == jogo_da_velha[2][coluna] == jogo_da_velha[3][coluna] != "_":
            return True
    if jogo_da_velha[0][0] == jogo_da_velha[1][1] == jogo_da_velha[2][2] == jogo_da_velha[3][3] != "_":
        return True
    if jogo_da_velha[0][3] == jogo_da_velha[1][2] == jogo_da_velha[2][1] == jogo_da_velha[3][0] != "_":
        return True
    return False

i = 0
desenhar_tabuleiro()
while True:
    i += 1
    jogada(variar_jogador(i))
    desenhar_tabuleiro()
    if ganhou():
        print("O jogador venceu!")
        break