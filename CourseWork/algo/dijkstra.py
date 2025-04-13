from typing import List, Tuple, Optional
import heapq

def dijkstra(graph: List[List[int]], start: int, end: int) -> Tuple[Optional[List[int]], Optional[int]]:
    """
    Находит кратчайший путь от start до end в графе, заданном матрицей смежности.
    Временная сложность: O(V^2), где V - число вершин.
    Возвращает: (путь, длина пути) или (None, None), если пути нет.
    """
    V = len(graph)
    distances = [float('inf')] * V
    distances[start] = 0
    prev = [None] * V
    visited = [False] * V
    
    for _ in range(V):
        min_dist = float('inf')
        u = -1
        for v in range(V):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                u = v
        if u == -1:
            break
        visited[u] = True
        for v in range(V):
            if not visited[v] and graph[u][v] > 0 and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]
                prev[v] = u
    
    if distances[end] == float('inf'):
        return None, None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    
    return path, distances[end]