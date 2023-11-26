import random
import pygame
import time
    
largura = 600
altura = 600

manter_conhecimento = True

cor_cinza = (128, 128, 128)
cor_branca = (255, 255, 255)
cor_preto = (0, 0, 0)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_azul = (0, 0, 255)
numero_cor_casa_percorrida = 10 # numero_cor_casa_percorrida da cor a ser preenchida quand percorrer o labirinto

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Labirinto')


def gerar_labirinto():
    return [
    [3, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

def esconder_gato(labirinto):
    coordenadas_caminho = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 1:
                coordenadas_caminho.append((i, j))

    coordenadas_caminho.pop()
    
    coordenada_gato = random.choice(coordenadas_caminho)
    labirinto[coordenada_gato[0]][coordenada_gato[1]] = 2
    return labirinto


def desenhar_labirinto(labirinto):
    janela.fill(cor_branca)

    tamanho_celula = largura // len(labirinto[0])

    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[0])):
            if linha < len(labirinto) and coluna < len(labirinto[0]):
                if labirinto[linha][coluna] == 1:
                    cor = cor_preto 
                elif labirinto[linha][coluna] == 2:
                    cor = cor_azul
                elif labirinto[linha][coluna] == 3:
                    cor = cor_verde
                elif labirinto[linha][coluna] <= -1:
                    cor = (255, -(labirinto[linha][coluna]), 255 + (labirinto[linha][coluna]))
                else:
                    cor = cor_cinza
                pygame.draw.rect(janela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()
    pygame.time.delay(100)  # Adiciona um pequeno atraso para visualizar a busca


def dfs(labirinto, linha, coluna):

    global numero_cor_casa_percorrida

    if not manter_conhecimento:
        labirinto = [row[:] for row in labirinto]
        
    if linha < 0 or coluna < 0 or linha >= len(labirinto) or coluna >= len(labirinto[0]) or labirinto[linha][coluna] <= 0:
        return False

    encontrado = labirinto[linha][coluna] == 2

    labirinto[linha][coluna] = 3;    
    desenhar_labirinto(labirinto)

    labirinto[linha][coluna] = -(numero_cor_casa_percorrida)

    if encontrado:
        return True
    
    resultado = dfs(labirinto, linha, coluna - 1) or dfs(labirinto, linha - 1, coluna) or dfs(labirinto, linha, coluna + 1) or dfs(labirinto, linha + 1, coluna) 

    numero_cor_casa_percorrida = int ((numero_cor_casa_percorrida + 13) % 255)
    print
    return resultado


def main():
    rodando = True
    labirinto = esconder_gato(gerar_labirinto())
    
    desenhar_labirinto(labirinto)
    time.sleep(1)

    print("Começando a busca no labirinto...")
    encontrou = dfs(labirinto, 0, 0)
    if encontrou:
        print("Gato encontrado!")
    else:
        print("Gato não encontrado!")

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

    pygame.quit()

if __name__ == "__main__":
    main()
