from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Funções do jogo
def cria_tabuleiro():
    tabuleiro = []
    for _ in range(5):
        linha = ["O"] * 5
        tabuleiro.append(linha)
    return tabuleiro

def imprime_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def posicionar_navios(tabuleiro, num_navios):
    for _ in range(num_navios):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if tabuleiro[x][y] == "X":
            continue
        tabuleiro[x][y] = "X"

def atacar(tabuleiro, x, y):
    if tabuleiro[x][y] == "X":
        tabuleiro[x][y] = "H"  # Navio atingido
        return True
    else:
        tabuleiro[x][y] = "M"  # Água atingida
        return False

# Variáveis globais para o estado do jogo
tabuleiro_jogador1 = cria_tabuleiro()
tabuleiro_jogador2 = cria_tabuleiro()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar_jogo', methods=['POST'])
def iniciar_jogo():
    global tabuleiro_jogador1, tabuleiro_jogador2

    # Reiniciar os tabuleiros e começar o jogo
    tabuleiro_jogador1 = cria_tabuleiro()
    tabuleiro_jogador2 = cria_tabuleiro()
    posicionar_navios(tabuleiro_jogador1, 3)
    posicionar_navios(tabuleiro_jogador2, 3)

    return redirect(url_for('tabuleiro'))

@app.route('/tabuleiro')
def tabuleiro():
    return render_template('tabuleiro.html', tabuleiro=tabuleiro_jogador1)

@app.route('/jogada', methods=['POST'])
def jogada():
    global tabuleiro_jogador1, tabuleiro_jogador2

    x = int(request.form['x'])
    y = int(request.form['y'])
    resultado = atacar(tabuleiro_jogador2, x, y)

@app.route('/ataque', methods=['POST'])
def ataque():
    global tabuleiro_jogador1, tabuleiro_jogador2

    x = int(request.form['x'])
    y = int(request.form['y'])

    # Verificar se o jogador já fez essa jogada (opcional)
    if tabuleiro_jogador1[x][y] == "H" or tabuleiro_jogador1[x][y] == "M":
        return render_template('tabuleiro.html', tabuleiro=tabuleiro_jogador1, resultado=False)

    resultado = atacar(tabuleiro_jogador1, x, y)

    # Lógica para atualizar o estado do jogo (verificar vitória, derrota, etc.)

    return render_template('tabuleiro.html', tabuleiro=tabuleiro_jogador1, resultado=resultado)

@app.route('/ataque_jogador2', methods=['POST'])
def ataque_jogador2():
    x = int(request.form['x'])  # Obtenha as coordenadas x e y do formulário
    y = int(request.form['y'])
    resultado = processar_ataque_jogador2(x, y, tabuleiro_jogador2)  # Chame a função processar_ataque_jogador2 com todos os argumentos

    # Você pode adicionar mais lógica aqui, como verificar o resultado do ataque e atualizar o estado do jogo.

    return render_template('tabuleiro_jogador2.html', resultado=resultado)



def processar_ataque_jogador2(x, y, tabuleiro_jogador2):
    if tabuleiro_jogador2[x][y] == "X":
        tabuleiro_jogador2[x][y] = "H"  # Atualize para "H" para marcar o navio como atingido.
        resultado = "Jogador 2 acertou um navio!"
    else:
        tabuleiro_jogador2[x][y] = "M"  # Atualize para "M" para marcar a água como atingida.
        resultado = "Jogador 2 errou o tiro."
    
    # Adicione mais lógica aqui, se necessário, para verificar o resultado do jogo, por exemplo, se todos os navios do jogador 2 foram afundados.

    return resultado


  
   
   # Atualize o estado do jogo, se necessário
    

def cria_tabuleiro_jogador2():
    tabuleiro = []
    for _ in range(5):
        linha = ["O"] * 5
        tabuleiro.append(linha)
    return tabuleiro

def posicionar_navios_jogador2(tabuleiro, num_navios):
    for _ in range(num_navios):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if tabuleiro[x][y] == "X":
            continue
        tabuleiro[x][y] = "X"

@app.route('/tabuleiro_jogador2')
def tabuleiro_jogador2():
    tabuleiro_jogador2 = cria_tabuleiro_jogador2()
    posicionar_navios_jogador2(tabuleiro_jogador2, 3)  # Posicione os navios de acordo com as regras
    mensagem = None  # Adicione uma mensagem se desejar
    return render_template('tabuleiro_jogador2.html', tabuleiro=tabuleiro_jogador2, mensagem=mensagem)



if __name__ == '__main__':
    app.run(debug=True)
