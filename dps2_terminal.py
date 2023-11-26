import pygame
import time

largura = 600
altura = 600
tamanho_celula = largura // 5
linhas = altura // tamanho_celula
colunas = largura // tamanho_celula

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Labirinto')

cor_branca = (255, 255, 255)
cor_preto = (0, 0, 0)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_azul = (0, 0, 255)

def desenhar_labirinto(labirinto):
    janela.fill(cor_branca)
    for linha in range(linhas):
        for coluna in range(colunas):
            if linha < len(labirinto) and coluna < len(labirinto[0]):
                if labirinto[linha][coluna] == 1:
                    cor = cor_preto 
                elif labirinto[linha][coluna] == 2:
                    cor = cor_azul
                elif labirinto[linha][coluna] == -1:
                    cor = cor_vermelha
                else:
                    cor = cor_branca
                pygame.draw.rect(janela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()

def dfs(labirinto, linha, coluna):

    l = [row[:] for row in labirinto]
        
    if linha < 0 or coluna < 0 or linha >= len(l) or coluna >= len(l[0]) or l[linha][coluna] <= 0:
        return False

    encontrado = l[linha][coluna] == 2

    l[linha][coluna] = -1
    desenhar_labirinto(l)

    if encontrado:
        print('Gato encontrado!')
        return True
    
    pygame.draw.rect(janela, cor_verde, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()
    pygame.time.delay(400)  # Adiciona um pequeno atraso para visualizar a busca

    print(l)

    return dfs(l, linha + 1, coluna) or dfs(l, linha - 1, coluna) or dfs(l, linha, coluna + 1) or dfs(l, linha, coluna - 1)

def main():

    labirinto = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 2, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    rodando = True
    desenhar_labirinto(labirinto)
    time.sleep(1)

    print("Começando a busca no labirinto...")
    dfs(labirinto, 0, 0)

    print(labirinto)

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

    pygame.quit()

if __name__ == "__main__":
    main()
