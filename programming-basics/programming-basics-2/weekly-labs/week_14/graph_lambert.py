"""Temp"""

import graph_linked as gl
import graph as g


def read_file(filename: str) -> list:
    """
    Read a file and return a list
    """
    return g.read_file(filename)


def create_graph(arr: list) -> gl.LinkedDirectedGraph:
    """
    Build a LinkedDirectedGraph with vertices for each rating
    and directed edges where 1 <= to - from <= 3.
    """
    gh = gl.LinkedDirectedGraph()
    for a in arr:
        gh.addVertex(a)
    n = len(arr)
    for i, a in enumerate(arr):
        for j in range(i+1, n):
            b = arr[j]
            diff = b - a
            if 1 <= diff <= 3:
                gh.addEdge(a, b, None)
            elif diff > 3:
                break
    return gh


def find_combinations(graph: gl.LinkedDirectedGraph) -> (set, int):
    """
    Perform DFS over LinkedDirectedGraph to find all paths.
    Returns (set of tuples, count).
    """
    verts = sorted(v.getLabel() for v in graph.vertices())
    if not verts:
        return set(), 0
    start, end = verts[0], verts[-1]
    paths = set()

    def dfs(current, path):
        if current == end:
            paths.add(tuple(path))
            return
        for nbr in graph.neighboringVertices(current):
            dfs(nbr.getLabel(), path + [nbr.getLabel()])

    dfs(start, [start])
    return paths, len(paths)
