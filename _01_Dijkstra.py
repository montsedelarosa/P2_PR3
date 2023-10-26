import heapq

def dijkstra(graph, start):
    # Inicializar distancias y conjunto de nodos visitados
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    # Crear una cola de prioridad (min-heap) para explorar nodos
    priority_queue = [(0, start)]

    while priority_queue:
        # Obtener el nodo con la distancia mínima
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si ya hemos visitado este nodo, continuamos
        if current_node in visited:
            continue

        # Marcar el nodo como visitado
        visited.add(current_node)

        # Explorar los nodos adyacentes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si encontramos una distancia menor, actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)

print("Distancias más cortas desde el nodo de inicio (", start_node, "):")
for node, distance in result.items():
    print("Hasta", node, ":", distance)
