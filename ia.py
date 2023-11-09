import matplotlib.pyplot as plt
# Função de busca em profundidade
def busca_gato_labirinto(labirinto, linha, coluna, visitados, caminho_atual):
    if linha < 0 or coluna < 0 or linha >= len(labirinto) or coluna >= len(labirinto[0]) or labirinto[linha][coluna] == 0 or (linha, coluna) in visitados:
        return
    visitados.add((linha, coluna))
    caminho_atual.append((linha, coluna))
    print(f'Explorando posição: ({linha}, {coluna})')
    print('Caminho percorrido até agora:', caminho_atual)
    busca_gato_labirinto(labirinto, linha+1, coluna, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha-1, coluna, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha, coluna+1, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha, coluna-1, visitados, caminho_atual)
    caminho_atual.pop()

# Função para desenhar o labirinto
def desenhar_labirinto(labirinto, caminho):
    fig, ax = plt.subplots()
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='white'))
            else:
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, color='black'))
    for pos in caminho:
        ax.add_patch(plt.Rectangle((pos[1], -pos[0]-1), 1, 1, color='lightgreen'))
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

# Definindo o labirinto como uma matriz
labirinto = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

# Iniciando a busca a partir da posição inicial
visitados = set()
caminho_atual = []
print("Começando a busca pelo gato no labirinto...")
busca_gato_labirinto(labirinto, 0, 0, visitados, caminho_atual)

# Desenhando o labirinto com o caminho percorrido
plt.draw()
desenhar_labirinto(labirinto, caminho_atual)
