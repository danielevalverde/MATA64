import random
import pygame
import time
from collections import deque

largura = 600
altura = 600

qtd_visitados = 0

cor_cinza = (128, 128, 128)
cor_branca = (255, 255, 255)
cor_preto = (0, 0, 0)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)
cor_azul = (0, 0, 255)
cor_percorrido = (255, 10, 245)
cor_a_ser_percorrido = (255, 195, 60)

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Labirinto')


def gerar_labirinto():
    # return [
    #     [3,1,1,0,1,1,0,1,1,1,0,1],
    #     [0,0,1,0,1,1,0,1,1,1,0,1],
    #     [0,0,1,0,1,1,0,0,1,0,0,1],
    #     [1,0,1,0,0,1,0,0,1,0,0,1],
    #     [1,0,1,1,1,1,1,1,1,1,1,1],
    #     [1,1,1,0,1,0,0,1,0,1,0,0],
    #     [1,1,1,0,1,1,0,1,0,1,1,0],
    #     [0,1,0,0,0,1,0,1,0,1,0,0],
    #     [0,0,0,0,0,1,0,1,0,1,1,1],
    #     [1,1,1,1,0,0,0,1,0,0,0,0],
    #     [0,1,0,0,0,0,0,1,0,1,1,1],
    #     [1,1,1,1,1,1,1,1,1,1,1,1],
    # ]
    
    # return [
    #     [3, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    #     [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    #     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    #     [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    #     [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    #     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    #     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    #     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    # ]
    
    # return [
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    #     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
    #     [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1], 
    #     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], 
    #     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], 
    #     [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], 
    #     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
    #     [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
    #     [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    #     [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1], 
    #     [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1], 
    #     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
    #     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1], 
    #     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1], 
    #     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1], 
    #     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1], 
    #     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1], 
    #     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    #     [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], 
    #     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
    #     [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], 
    #     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    # ]
    
    return generate_maze(12)


def generate_maze(size):
    maze = [[0] * (2*size + 1) for _ in range(2*size + 1)]

    for i in range(2*size + 1):
        for j in range(2*size + 1):
            if i % 2 == 0 or j % 2 == 0:
                maze[i][j] = 1

    stack = [(1, 1)]
    visited = set()

    def is_valid(cell):
        x, y = cell
        return 0 < x < 2*size and 0 < y < 2*size and (x, y) not in visited

    def get_neighbors(cell):
        x, y = cell
        return [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]

    while stack:
        current_cell = stack[-1]
        x, y = current_cell

        neighbors = [neighbor for neighbor in get_neighbors(current_cell) if is_valid(neighbor) and neighbor not in visited]

        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell

            maze[(x + nx) // 2][(y + ny) // 2] = 0
            visited.add(next_cell)
            stack.append(next_cell)
        else:
            stack.pop()
    # print
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
        
    return maze

def esconder_gato(labirinto):
    coordenadas_caminho = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 1:
                coordenadas_caminho.append((i, j))

    del coordenadas_caminho[0]
    
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
                elif labirinto[linha][coluna] == -1:
                    cor = cor_percorrido
                elif labirinto[linha][coluna] == 4:
                    cor = cor_a_ser_percorrido
                else:
                    cor = cor_cinza
                pygame.draw.rect(janela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.update()
    pygame.time.delay(100)  # Adiciona um pequeno atraso para visualizar a busca


def dfs(labirinto, linha, coluna):

    global numero_cor_casa_percorrida

    manter_conhecimento = True
    if not manter_conhecimento:
        labirinto = [row[:] for row in labirinto]
        
    if linha < 0 or coluna < 0 or linha >= len(labirinto) or coluna >= len(labirinto[0]) or labirinto[linha][coluna] <= 0:
        return False

    encontrado = labirinto[linha][coluna] == 2

    labirinto[linha][coluna] = 3;
    
    # colore proximas casa a ser percorrida
    if linha-1 >= 0 and labirinto[linha-1][coluna] > 0 and labirinto[linha-1][coluna] != 2:
        labirinto[linha-1][coluna] = 4
    if coluna-1 >= 0 and labirinto[linha][coluna-1] > 0 and labirinto[linha][coluna-1] != 2:
        labirinto[linha][coluna-1] = 4
    if linha+1 < len(labirinto) and labirinto[linha+1][coluna] > 0 and labirinto[linha+1][coluna] != 2:
        labirinto[linha+1][coluna] = 4
    if coluna+1 < len(labirinto[0]) and labirinto[linha][coluna+1] > 0 and labirinto[linha][coluna+1] != 2:
        labirinto[linha][coluna+1] = 4
    
    global qtd_visitados
    qtd_visitados += 1 
    desenhar_labirinto(labirinto)

    labirinto[linha][coluna] = -1

    if encontrado:
        return True
    
    return dfs(labirinto, linha, coluna - 1) or dfs(labirinto, linha - 1, coluna) or dfs(labirinto, linha, coluna + 1) or dfs(labirinto, linha + 1, coluna) 

def bfs(labirinto, linha, coluna):
    queue = deque([(linha, coluna)])
    visited = set()

    while queue:
        linha, coluna = queue.popleft()

        if (linha, coluna) not in visited and labirinto[linha][coluna] > 0:
            visited.add((linha, coluna))
            
            encontrado = labirinto[linha][coluna] == 2
            
            labirinto[linha][coluna] = 3
            global qtd_visitados
            qtd_visitados += 1
            
            # colore proximas casa a ser percorrida
            if linha-1 >= 0 and labirinto[linha-1][coluna] > 0 and labirinto[linha-1][coluna] != 2:
                labirinto[linha-1][coluna] = 4
            if coluna-1 >= 0 and labirinto[linha][coluna-1] > 0 and labirinto[linha][coluna-1] != 2:
                labirinto[linha][coluna-1] = 4
            if linha+1 < len(labirinto) and labirinto[linha+1][coluna] > 0 and labirinto[linha+1][coluna] != 2:
                labirinto[linha+1][coluna] = 4
            if coluna+1 < len(labirinto[0]) and labirinto[linha][coluna+1] > 0 and labirinto[linha][coluna+1] != 2:
                labirinto[linha][coluna+1] = 4
            
            desenhar_labirinto(labirinto)
            
            if encontrado:
                return True  # Gato encontrado
            else:
                labirinto[linha][coluna] = -1

            # Adiciona vizinhos à fila
            neighbors = [(linha, coluna - 1), (linha - 1, coluna), (linha, coluna + 1), (linha + 1, coluna)]
            queue.extend(neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(labirinto)
                          and 0 <= neighbor[1] < len(labirinto[0]))

    return False  # Gato não encontrado


def comparar_buscas(labirinto):
    coordenadas_caminho = []
    for i in range(1, len(labirinto)-1):
        for j in range(1, len(labirinto[0])-1):
            if labirinto[i][j] == 1:
                coordenadas_caminho.append((i, j))

    del coordenadas_caminho[0]
    
    coordenadas_caminho.reverse()
    global qtd_visitados
    
    qtd_bfs = 0
    qtd_dfs = 0
    qtd_bfs_ganhou = 0
    qtd_dfs_ganhou = 0
    
    for i in range(len(coordenadas_caminho)):
        labirinto[coordenadas_caminho[i][0]][coordenadas_caminho[i][1]] = 2
        
        qtd_visitados = 0
        labirinto_bfs = [row[:] for row in labirinto]
        encontrou = bfs(labirinto_bfs, 0, 0)
        qtd_bfs_atual = qtd_visitados
        qtd_bfs += qtd_visitados
        
        qtd_visitados = 0
        labirinto_dfs = [row[:] for row in labirinto]
        encontrou = dfs(labirinto_dfs, 0, 0)
        qtd_dfs_atual = qtd_visitados
        qtd_dfs += qtd_visitados
        
        labirinto[coordenadas_caminho[i][0]][coordenadas_caminho[i][1]] = 1
        
        if qtd_bfs_atual < qtd_dfs_atual:
            qtd_bfs_ganhou += 1
        elif qtd_bfs_atual > qtd_dfs_atual:
            qtd_dfs_ganhou += 1
        else:
            qtd_bfs_ganhou += 1
            qtd_dfs_ganhou += 1
            
        print(f"BFS: {qtd_bfs_ganhou} DFS: {qtd_dfs_ganhou}")
        
    
    print(f"Quantidade de casas visitadas BFS: {qtd_bfs}")
    print(f"Quantidade de casas visitadas DFS: {qtd_dfs}")
    
    
def main():
    
    # return comparar_buscas(gerar_labirinto())

    rodando = True
    labirinto = esconder_gato(gerar_labirinto())
    
    print("Começando a busca no labirinto...")
    
    encontrou = dfs(labirinto, 0, 0)
    # encontrou = bfs(labirinto, 0, 0)
    
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
