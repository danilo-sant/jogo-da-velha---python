branco = ' '
token = ["X", "O"]


def criarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print('|'.join(board[i]))
        if i < 2:
            print('-----')


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if 1 <= n <= 3:
            return n - 1
        else:
            print('Número precisa esta entre 1 e 3!')
            return getInputValido(mensagem)
    except:
        print('Número não válido!')
        getInputValido(mensagem)


def verificaMovimento(board, i, j):
    if board[i][j] == branco:
        return True
    else:
        return False


def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]


def verificaGanhador(board):
    # Verificar Linha
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco:
            return board[i][0]
    # Verificar Coluna
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != branco:
            return board[0][j]
    # Verificar Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != branco:
        return board[0][0]
    # Verificar Diagonal Secundária
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != branco:
        return board[0][2]
    # verifica se todas as colunas preenchidas e deu EMPATE
    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False
    return 'EMPATE'
