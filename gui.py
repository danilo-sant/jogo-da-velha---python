import pygame

from jogo_da_velha import criarBoard, fazMovimento, printBoard, verificaGanhador, verificaMovimento
from minimax import movimentoIA

pygame.font.init()


def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600 / 3

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i * tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0, 0, 0), (i * tamanho, 0), (i * tamanho, height))

    # desenhar X e O
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont('comicsans', 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (128, 0, 0))
            win.blit(text, ((x + 75), (y + 75)))


def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)


def main():
    win = pygame.display.set_mode((600, 600))  # criar tela
    pygame.display.set_caption('Jogo da Velha')  # definir título da tela

    board = criarBoard()

    redraw_window(win, board)  # redesenhamos a tela
    pygame.display.update()  # atualizamos a tela

    jogador = 0

    ganhador = verificaGanhador(board)  # verifica se tem ganhador

    while not ganhador:
        printBoard(board)
        if jogador == 0:
            jogou = False
            while not jogou:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()  # capta o click do mouse
                        i = int(pos[1] / 200)
                        j = int(pos[0] / 200)
                        jogou = True
        else:
            i, j = movimentoIA(board, jogador)

        if verificaMovimento(board, i, j):
            fazMovimento(board, i, j, jogador)
            jogador = (jogador + 1) % 2  # Trocar Jogador

        ganhador = verificaGanhador(board)

        redraw_window(win, board)
        pygame.display.update()

        if ganhador != True and ganhador != False:
            if ganhador != 'X' and ganhador != 'O':
                texto = ('O jogo terminou ' + str(ganhador))
                font = pygame.font.SysFont('comicsans', 30)
                text = font.render(texto, 1, (128, 0, 0))
                win.blit(text, (10, 10))
                pygame.display.update()
            else:
                texto = ('O ganhador foi ' + str(ganhador))
                font = pygame.font.SysFont('comicsans', 30)
                text = font.render(texto, 1, (128, 0, 0))
                win.blit(text, (10, 10))
                pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                return


main()
