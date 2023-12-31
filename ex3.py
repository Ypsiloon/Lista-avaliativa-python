import random

arquivo = "C:\\Users\\bipef\\OneDrive\\Documentos\\bipe python\\python listas\\lista_palavras.txt"

def le_arquivo(arq):
    """
    Lê as palavras de um arquivo de texto.

    Args:
        arq: O caminho do arquivo.

    Retorna:
        lista: Uma lista de palavras lidas do arquivo.
    """
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]

lista = le_arquivo(arquivo)

def escolher_palavra():
    """
    Escolhe aleatoriamente uma palavra da lista de palavras.

    Retorna:
        str: A palavra escolhida.
    """
    numero_letras = int(input("Digite a quantidade de letras que deseja ter na palavra: "))
    palavras_possiveis = [palavra for palavra in lista if len(palavra) == numero_letras]

    if not palavras_possiveis:
        print("Palavra com esta quantidade de letras não foi encontrada... Sorteando outra palavra")
        return random.choice(lista)
    else:
        print("Palavra sorteada!")
        return random.choice(palavras_possiveis)

def inicia_letras(palavra):
    """
    Inicializa as letras da palavra ocultas com underscores.

    Args:
        palavra: A palavra oculta.

    Retorna:
        lista: Uma lista de underscores representando as letras ocultas.
    """
    return ["_" for _ in palavra]

def verificar_palavra(palavra, chute):
    """
    Verifica as letras da palavra e fornece dicas de cores.

    Args:
        palavra: A palavra a ser adivinhada.
        chute: O chute do jogador.

    Retorna:
        lista: Uma lista de dicas de cores para cada letra do chute.
    """
    dica = []
    for i, letra in enumerate(palavra):
        if letra == chute[i]:
            dica.append("verde")
        elif letra in chute and letra != chute[i]:
            dica.append("amarelo")
        else:
            dica.append("cinza")
    return dica

def colorir_palavra(palavra, dica):
    """
    Colore a palavra com base nas dicas de cores.

    Args:
        palavra: A palavra a ser colorida.
        dica: Uma lista de dicas de cores para cada letra da palavra.

    Retorna:
        str: A palavra colorida com códigos de cores ANSI.
    """
    palavra_colorida = ""
    for letra, cor in zip(palavra, dica):
        if cor == "verde":
            palavra_colorida += f"\033[92m{letra}\033[m"
        elif cor == "amarelo":
            palavra_colorida += f"\033[93m{letra}\033[m"
        else:
            palavra_colorida += f"\033[90m{letra}\033[m"
    return palavra_colorida

def letras_usadas(teclado, palavra_sorteada, chute):
    """
    Registra as letras usadas pelo jogador e remove do teclado.

    Args:
        teclado: Uma lista de letras disponíveis.
        palavra_sorteada: A palavra a ser adivinhada.
        chute: O chute do jogador.

    """
    teclado_colorido = teclado.copy()
    for letra in chute:
        if letra not in palavra_sorteada:
            for i in range(len(teclado)):
                if teclado[i] == letra:
                    teclado.pop(i)
                    break

letras_corretas = set()
vida = 6
perdeu = ganhou = False
historico = []
teclado = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

print("----------------------")
print("| Bem vindo ao Termo |")
print("----------------------")

palavra_sorteada = escolher_palavra()
print("Palavra sorteada (para testes): " + palavra_sorteada)

letras_certas = inicia_letras(palavra_sorteada)
print(letras_certas)

while not perdeu and not ganhou:
    teclado_bonito = ' '.join(map(str, teclado))
    print("Teclado Disponivel:", teclado_bonito)
    chute = input("Digite uma palavra: ").lower()
    historico.append(chute)
    remover = letras_usadas(teclado, palavra_sorteada, chute)

    dica = verificar_palavra(palavra_sorteada, chute)
    palavra_colorida = colorir_palavra(palavra_sorteada, dica)

    for x in historico:
        print(colorir_palavra(x, verificar_palavra(palavra_sorteada, x)))

    if chute == palavra_sorteada:
        print("Você venceu!!!")
        ganhou = True
        break
    elif chute not in palavra_sorteada:
        vida -= 1
        print(f"Você errou, ainda possui {vida} chances")
        
    for letra in chute:
        if letra in palavra_sorteada:
            letras_corretas.add(letra)
    print("Letras corretas ", letras_corretas)

    perdeu = vida == 0

print(f"A palavra correta era: {palavra_sorteada}")
