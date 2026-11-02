"""Temp"""

from graph import Graph
from shortest_paths_dijkstra import dijkstras_shortest_path
import heapq
import math


def read_file(filename: str):
    """
    Read data from Freemans_EIES-1_n48.txt file.
    Format: Matrix where each value represents relationship strength (0-4)

    Args:
        filename (str): Path to Freemans_EIES-1_n48.txt

    Returns:
        list: 2D list representing the relationship matrix
    """
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            row = [int(val) for val in line.split()]
            if row:
                matrix.append(row)
    return matrix


def graph_paths_1(matrix: list, source_researcher: int):
    """
    Build a Graph_map graph and find the shortest paths using Dijkstra's algorithm.

    Args:
        matrix (list): 2D list representing the relationship matrix
        source_researcher (int): Index of the source researcher (0-based)

    Returns:
        dict: Dictionary mapping researcher indices to their distance from the source
        dict: Dictionary mapping researcher indices to the path from the source
    """
    g = Graph(directed=True)
    vertices = [g.insert_vertex(i) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] > 0:
                weight = 5 - matrix[i][j]
                g.insert_edge(vertices[i], vertices[j], weight)

    source = vertices[source_researcher]
    distances = {vertex: math.inf for vertex in g.vertices()}
    previous_vertices = {vertex: None for vertex in g.vertices()}
    distances[source] = 0
    dict_vertex_length = {source: 0}

    while dict_vertex_length:
        current_vertex = min(dict_vertex_length, key=dict_vertex_length.get)
        del dict_vertex_length[current_vertex]

        for edge in g.incident_edges(current_vertex):
            adj_vertex = edge.opposite(current_vertex)
            length_to_vertex = edge.element()

            if distances[adj_vertex] > distances[current_vertex] + length_to_vertex:
                distances[adj_vertex] = distances[current_vertex] + length_to_vertex
                dict_vertex_length[adj_vertex] = distances[adj_vertex]
                previous_vertices[adj_vertex] = current_vertex
    distance_dict = {}
    paths_dict = {}
    for v in vertices:
        researcher_id = v.element()
        if v is source:
            distance_dict[researcher_id] = 0
            paths_dict[researcher_id] = [researcher_id]
        elif distances[v] != math.inf:
            distance_dict[researcher_id] = distances[v]
            path = []
            current = v
            while current is not None:
                path.append(current.element())
                current = previous_vertices[current]
            path.reverse()
            paths_dict[researcher_id] = path
        else:
            distance_dict[researcher_id] = float('inf')
            paths_dict[researcher_id] = []
    return distance_dict, paths_dict


def graph_paths_2(matrix, source_researcher):
    """
    Build a Graph_easy graph and find shortest paths using Dijkstra's algorithm.

    Args:
        matrix (list): 2D list representing the relationship matrix
        source_researcher (int): Index of the source researcher (0-based)

    Returns:
        dict: Dictionary mapping researcher indices to their distance from the source
        dict: Dictionary mapping researcher indices to the path from the source
    """
    num_researchers = len(matrix)
    graph = [[] for _ in range(num_researchers)]
    for i in range(num_researchers):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] > 0:
                weight = 5 - matrix[i][j]
                graph[i].append((j, weight))
    distances = {i: float('infinity') for i in range(num_researchers)}
    previous = {i: None for i in range(num_researchers)}
    distances[source_researcher] = 0
    to_visit = {source_researcher: 0}
    while to_visit:
        current = min(to_visit, key=to_visit.get)
        current_distance = to_visit[current]
        del to_visit[current]
        for neighbor, weight in graph[current]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                to_visit[neighbor] = distance
    paths = {}
    for i in range(num_researchers):
        if i == source_researcher:
            paths[i] = [i]
        elif distances[i] == float('infinity'):
            paths[i] = []
        else:
            path = []
            current = i
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            paths[i] = path
    return distances, paths


if __name__ == '__main__':
    filename = "Freemans_EIES-1_n48.txt"
    matrix = read_file(filename)
    print(matrix)
    distances_1, paths_1 = graph_paths_1(matrix, 0)
    print(distances_1)
    print(paths_1)
    distances_2, paths_2 = graph_paths_2(matrix, 0)
    print(distances_2)
    print(paths_2)
    print(distances_1 == distances_2)
    print(paths_1 == paths_2)
