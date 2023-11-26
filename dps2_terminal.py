import pygame
import time


labirinto = [
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]
    
largura = 600
altura = 600
tamanho_celula = largura // len(labirinto[0])
linhas = altura // tamanho_celula
colunas = largura // tamanho_celula

manter_conhecimento = True

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Labirinto')

cor_cinza = (128, 128, 128)
cor_branca = (255, 255, 255)
cor_preto = (0, 0, 0)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_azul = (0, 0, 255)

numero_cor_casa_percorrida = 10 # numero_cor_casa_percorrida da cor a ser preenchida quand percorrer o labirinto

def desenhar_labirinto(labirinto):
    janela.fill(cor_branca)
    for linha in range(linhas):
        for coluna in range(colunas):
            if linha < len(labirinto) and coluna < len(labirinto[0]):
                if labirinto[linha][coluna] == 1:
                    cor = cor_preto 
                elif labirinto[linha][coluna] == 2:
                    cor = cor_azul
                elif labirinto[linha][coluna] <= -1:
                    cor = (255, -(labirinto[linha][coluna]), 255 + (labirinto[linha][coluna]))
                else:
                    cor = cor_cinza
                pygame.draw.rect(janela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()

def dfs(labirinto, linha, coluna):

    global numero_cor_casa_percorrida

    if not manter_conhecimento:
        labirinto = [row[:] for row in labirinto]
        
    if linha < 0 or coluna < 0 or linha >= len(labirinto) or coluna >= len(labirinto[0]) or labirinto[linha][coluna] <= 0:
        return False

    encontrado = labirinto[linha][coluna] == 2
    
    labirinto[linha][coluna] = -(numero_cor_casa_percorrida)
    desenhar_labirinto(labirinto)

    if encontrado:
        print('Gato encontrado!')
        return True
    
    pygame.draw.rect(janela, cor_verde, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()
    pygame.time.delay(100)  # Adiciona um pequeno atraso para visualizar a busca

    resultado = dfs(labirinto, linha, coluna - 1) or dfs(labirinto, linha - 1, coluna) or dfs(labirinto, linha, coluna + 1) or dfs(labirinto, linha + 1, coluna) 

    numero_cor_casa_percorrida = int ((numero_cor_casa_percorrida + 13) % 255)
    print
    return resultado


def main():
    rodando = True
    desenhar_labirinto(labirinto)
    time.sleep(1)

    print("Começando a busca no labirinto...")
    dfs(labirinto, 0, 0)

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

    pygame.quit()

if __name__ == "__main__":
    main()
