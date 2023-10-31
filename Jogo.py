import random

# Função para criar o tabuleiro vazio
def cria_tabuleiro():
    tabuleiro = []
    for _ in range(5):
        linha = ["O"] * 5
        tabuleiro.append(linha)
    return tabuleiro

# Função para imprimir o tabuleiro
def imprime_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

# Função para posicionar os navios no tabuleiro
def posicionar_navios(tabuleiro, num_navios):
    for _ in range(num_navios):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if tabuleiro[x][y] == "X":
            continue
        tabuleiro[x][y] = "X"

# Função para a vez do jogador atacar
def atacar(tabuleiro, x, y):
    if tabuleiro[x][y] == "X":
        tabuleiro[x][y] = "H"  # Navio atingido
        return True
    else:
        tabuleiro[x][y] = "M"  # Água atingida
        return False

# Função principal do jogo
def jogo_batalha_naval():
    print("Bem-vindo ao jogo de Batalha Naval!")
    tabuleiro_jogador1 = cria_tabuleiro()
    tabuleiro_jogador2 = cria_tabuleiro()
    posicionar_navios(tabuleiro_jogador1, 3)
    posicionar_navios(tabuleiro_jogador2, 3)

    while True:
        print("Tabuleiro do Jogador 1:")
        imprime_tabuleiro(tabuleiro_jogador1)
        x1 = int(input("Jogador 1, informe a linha (0-4): "))
        y1 = int(input("Jogador 1, informe a coluna (0-4): "))
        resultado1 = atacar(tabuleiro_jogador2, x1, y1)
        if resultado1:
            print("Jogador 1 acertou um navio!")
        else:
            print("Jogador 1 errou o tiro.")

        print("Tabuleiro do Jogador 2:")
        imprime_tabuleiro(tabuleiro_jogador2)
        x2 = int(input("Jogador 2, informe a linha (0-4): "))
        y2 = int(input("Jogador 2, informe a coluna (0-4): "))
        resultado2 = atacar(tabuleiro_jogador1, x2, y2)
        if resultado2:
            print("Jogador 2 acertou um navio!")
        else:
            print("Jogador 2 errou o tiro.")

        if all(linha.count("X") == 0 for linha in tabuleiro_jogador1):
            print("Jogador 2 venceu! Todos os navios do Jogador 1 foram afundados.")
            break
        if all(linha.count("X") == 0 for linha in tabuleiro_jogador2):
            print("Jogador 1 venceu! Todos os navios do Jogador 2 foram afundados.")
            break

if __name__ == "__main__":
    jogo_batalha_naval()
