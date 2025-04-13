import pytest
from algo.dijkstra import dijkstra

@pytest.fixture
def sample_graph():
    return [
        [0, 1, 4, 0],
        [1, 0, 2, 5],
        [4, 2, 0, 3],
        [0, 5, 3, 0]
    ]

def test_dijkstra_shortest_path(sample_graph):
    path, distance = dijkstra(sample_graph, 0, 3)
    assert path == [0, 1, 3], "Неверный путь"
    assert distance == 6, "Неверная длина пути"

def test_dijkstra_no_path():
    graph = [[0, 0], [0, 0]]
    path, distance = dijkstra(graph, 0, 1)
    assert path is None, "Путь должен отсутствовать"
    assert distance is None, "Длина пути должна быть None"

def test_dijkstra_same_vertex(sample_graph):
    path, distance = dijkstra(sample_graph, 0, 0)
    assert path == [0], "Путь должен быть только начальной вершиной"
    assert distance == 0, "Длина пути должна быть 0"