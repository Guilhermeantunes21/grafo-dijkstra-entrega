import heapq

grafo = {
    "Restaurante": {"Rua A": 2, "Rua B": 5},
    "Rua A": {"Praça": 1, "Restaurante": 2},
    "Rua B": {"Praça": 2, "Restaurante": 5},
    "Praça": {"Cliente": 3, "Rua A": 1, "Rua B": 2},
    "Cliente": {}
}

def dijkstra(grafo, inicio):
    dist = {v: float("inf") for v in grafo}
    dist[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        d, v = heapq.heappop(fila)

        for vizinho in grafo[v]:
            nova = d + grafo[v][vizinho]

            if nova < dist[vizinho]:
                dist[vizinho] = nova
                heapq.heappush(fila, (nova, vizinho))

    return dist

resultado = dijkstra(grafo, "Rua A")

print("Menor distância:", resultado["Restaurante"], "km")