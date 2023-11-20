import numpy as np

class Grafo: # classe para "montar" o grafo, atribuindo seus vertices e adjacencias
    def __init__(self, matriz_adjacencias):
        self.vertices = len(matriz_adjacencias)
        self.matriz_adjacencias = matriz_adjacencias

def DFS(graph, start, visited=None): # busca por profundidade, utilizando de recursividade
    if visited is None:
        visited = [False] * graph.vertices

    if not visited[start]:
        print(f"Visitando o vértice {start} e seus vizinhos: {vizinhos(graph, start)}")
        visited[start] = True

        for i in range(graph.vertices):
            if graph.matriz_adjacencias[start][i] == 1 and not visited[i]:
                DFS(graph, i, visited)

def vizinhos(graph, vertex): # buscando os vizinhos do vertice atual visitado
    vizim = [i for i in range(graph.vertices) if graph.matriz_adjacencias[vertex][i] == 1]
    return vizim

# Exemplo de matriz de adjacência
matriz_adjacencias = np.array([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
])

graph = Grafo(matriz_adjacencias) # chamando a classe para construir o grafo

print("Busca em Profundidade (DFS) a partir do vértice 0:") 

DFS(graph, 0) # chamando a função DFS