from colorama import init, Fore, Back

# Inicializa o colorama
init()

# Função de busca em profundidade
def busca_gato_labirinto(labirinto, linha, coluna, visitados, caminho_atual):
    if linha < 0 or coluna < 0 or linha >= len(labirinto) or coluna >= len(labirinto[0]) or labirinto[linha][coluna] == 0 or (linha, coluna) in visitados:
        return
    visitados.add((linha, coluna))
    caminho_atual.append((linha, coluna))
    print(f'Explorando posição: ({linha}, {coluna})')
    print('Caminho percorrido até agora:', caminho_atual)
    desenhar_labirinto_terminal(labirinto, caminho_atual)  # Adicionando a função de desenho aqui
    busca_gato_labirinto(labirinto, linha+1, coluna, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha-1, coluna, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha, coluna+1, visitados, caminho_atual)
    busca_gato_labirinto(labirinto, linha, coluna-1, visitados, caminho_atual)
    caminho_atual.pop()

# Função para desenhar o labirinto no terminal
def desenhar_labirinto_terminal(labirinto, caminho):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if (i, j) in caminho:
                print(Fore.GREEN + 'X', end=' ')
            elif labirinto[i][j] == 1:
                print(Back.WHITE + ' ', end=' ')
            else:
                print(Back.BLACK + ' ', end=' ')
        print(Back.RESET)

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
