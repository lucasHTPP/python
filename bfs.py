from collections import deque
import numpy as np

class Grafo:  # classe para "montar" o grafo, atribuindo seus vertices e adjacencias
    def __init__(self, matriz_adjacencias):
        self.vertices = len(matriz_adjacencias)
        self.matriz_adjacencias = matriz_adjacencias

def BFS(graph, start):  # busca por largura, utilizando de FILA
    visited = [False] * graph.vertices
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()

        if not visited[current_vertex]:
            print(f"Visitando o vértice {current_vertex} e seus vizinhos: {vizinhos(graph, current_vertex)}")
            visited[current_vertex] = True

            for i in range(graph.vertices):
                if graph.matriz_adjacencias[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)

def vizinhos(graph, vertex):  # buscando os vizinhos do vertice atual visitado
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

print("Busca em Largura (BFS) a partir do vértice 0:")

BFS(graph, 0) # chamando a função BFS
