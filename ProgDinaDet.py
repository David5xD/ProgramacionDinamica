import sys
from heapq import heapify, heappush, heappop

def progdinadet(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B': {'cost': inf, 'pred': []},
    'C': {'cost': inf, 'pred': []},
    'D': {'cost': inf, 'pred': []},
    'E': {'cost': inf, 'pred': []},
    'F': {'cost': inf, 'pred': []},
    'G': {'cost': inf, 'pred': []},
    'H': {'cost': inf, 'pred': []},
    'I': {'cost': inf, 'pred': []},
    'J': {'cost': inf, 'pred': []},
    'K': {'cost': inf, 'pred': []},
    'L': {'cost': inf, 'pred': []}}
    #Recoge la información de los nodos

    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(9):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    # Calcula el menor costo posible entre un nodo y el otro

    print("La menor distancia: " + str(node_data[dest]['cost']))
    print("El menor camino: " + str(node_data[dest]['pred'] + list(dest)))
    # Imprime la menor distancia y camino


if __name__ == "__main__":
    print("PRIMER EJERCICIO")
    graph = {
        'A':{'B':6, 'C':8, 'D':7},
        'B':{'A':6, 'E':9, 'F':10},
        'C':{'A':8, 'E':5, 'F':7, 'G':5, 'H':8},
        'D':{'A':7, 'G':8, 'H':14},
        'E':{'B':9, 'C':5, 'I':10, 'J':8},
        'F':{'B':10, 'C':6, 'I':7, 'J':9},
        'G':{'C':5, 'D':8, 'I':11, 'J':8, 'K':7},
        'H':{'C':6, 'D':14, 'J':12, 'K':6},
        'I':{'E':10, 'F':7, 'G':11, 'L':14},
        'J':{'E':8, 'F':9, 'G':8, 'H':12, 'L':6},
        'K':{'G':7, 'H':6, 'L':15},
        'L':{'I':14, 'J':6, 'K':15}
    }
    # Se recoge la información del grafo y sus conexiones

    source = 'A'
    destination = 'L'
    # Se recoge cual es el vertice de inicio y cual es el de destino

    progdinadet(graph,source,destination)
    # Se va a la función para calcular la menor distancia desde la fuente al destino

    print("SEGUNDO EJERCICIO")
    graph1 = {
        'A':{'B':10, 'C':8, 'D':7},
        'B':{'A':10, 'E':3, 'F':10},
        'C':{'A':8, 'E':5, 'F':7, 'G':11, 'H':8},
        'D':{'A':7, 'G':2, 'H':14},
        'E':{'B':3, 'C':5, 'I':10, 'J':8},
        'F':{'B':10, 'C':6, 'I':7, 'J':9},
        'G':{'C':11, 'D':2, 'I':11, 'J':8, 'K':5},
        'H':{'C':6, 'D':14, 'J':4, 'K':6},
        'I':{'E':10, 'F':7, 'G':11, 'L':6},
        'J':{'E':8, 'F':9, 'G':8, 'H':4, 'L':6},
        'K':{'G':5, 'H':6, 'L':11},
        'L':{'I':6, 'J':6, 'K':11}
    }

    source1 = 'A'
    destination1 = 'L'

    progdinadet(graph1,source1,destination1)