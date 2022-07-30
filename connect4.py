# define em constantes o tamanho da matriz
from re import I


NUM_LINHAS = 6
NUM_COLUNAS = 7

# matriz com as coordenados do jogo
jogo = []

# cria a matriz com as coordenadas do jogo (inicialmente, todas as posições estão vazias)
def cria_jogo():
    for i in range(NUM_LINHAS):
        jogo.append([])         # adiciona um array a cada linha do jogo
        for _ in range(NUM_COLUNAS):
            jogo[i].append(" ")     # adiciona um vazio a cada coluna

# monta (desenha) as coordenadas do jogo (com as peças)
def mostra_jogo():
    print()
    for i, linha in enumerate(jogo, start=1):
        print(f" {i}|", end="")
        for casa in linha:
            print(f" {casa} ", end="")
        print("|")
    print("  +---------------------+")    
    print("    1  2  3  4  5  6  7")

def linha_disponivel(coluna):
    disponivel = -1
    for i in range(NUM_LINHAS-1, -1, -1):
        if jogo[i][coluna] == " ":
            disponivel = i
            break
    return disponivel

def verifica_vencedor(simbolo):
    # verifica 4 colunas sequenciais na mesma linha (horizontal)
    for l in range(NUM_LINHAS):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c]==simbolo and jogo[l][c+1]==simbolo and jogo[l][c+2]==simbolo and jogo[l][c+3]==simbolo:
                return True

    # verifica 4 linhas sequenciais na mesma coluna (vertical)
    for l in range(NUM_LINHAS-3):
        for c in range(NUM_COLUNAS):
            if jogo[l][c]==simbolo and jogo[l+1][c]==simbolo and jogo[l+2][c]==simbolo and jogo[l+3][c]==simbolo:
                return True

    # verifica 4 casas sequenciais na transversal para baixo 
    for l in range(NUM_LINHAS-3):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c]==simbolo and jogo[l+1][c+1]==simbolo and jogo[l+2][c+2]==simbolo and jogo[l+3][c+3]==simbolo:
                return True

    # verifica 4 casas sequenciais na transversal para cima
    for l in range(NUM_LINHAS-1, NUM_LINHAS-4, -1):
        for c in range(NUM_COLUNAS-3):
            if jogo[l][c]==simbolo and jogo[l-1][c+1]==simbolo and jogo[l-2][c+2]==simbolo and jogo[l-3][c+3]==simbolo:
                return True


cria_jogo()
mostra_jogo()    

print("\nJogo Connect 4")
print("="*40)
print("Informe o número da coluna (1..7) ou 0 para sair")

contador = 1

while True:
    # operador ternário
    jogador = "x" if contador % 2 == 1 else "o"

    coluna = int(input(f"\nJogador '{jogador}', informe a coluna: "))

    if coluna == 0 or coluna > NUM_COLUNAS:
        break

    linha = linha_disponivel(coluna-1)

    if linha >= 0:
        jogo[linha][coluna-1] = jogador
        contador += 1
    else:
        print("Erro... Coluna já está totalmente preenchida. Jogue novamente...")
        continue

    mostra_jogo()

    if verifica_vencedor(jogador):
        print()
        print("*"*50)
        print(f"Parabéns Jogador '{jogador}'! Você é o vencedor!!")    
        break

    if contador == NUM_LINHAS*NUM_COLUNAS:
        print("Ah... deu empate...")
        break