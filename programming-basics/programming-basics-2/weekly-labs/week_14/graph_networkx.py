"""Temp"""


import networkx as nx
import graph as g

def read_file(filename: str) -> list:
    """Temp"""
    return g.read_file(filename)


def create_graph(arr: list) -> nx.DiGraph:
    """
    Creates a directed graph where adapters can connect to
    other adapters with joltage difference of 1-3.

    Args:
        arr: List of joltages (sorted)

    Returns:
        A NetworkX DiGraph where nodes are joltages and edges represent
        valid connections between adapters.
    """
    graph = nx.DiGraph()
    graph.add_nodes_from(arr)
    for i, current in enumerate(arr):
        for j in range(i + 1, len(arr)):
            next_j = arr[j]
            diff = next_j - current

            if 1 <= diff <= 3:
                graph.add_edge(current, next_j)
            elif diff > 3:
                break
    return graph


def find_combinations(gh: nx.DiGraph) -> (tuple, int):
    """
    Finds all possible combinations of adapters to connect from the outlet to the device.

    Uses NetworkX's built-in path finding algorithms to identify all valid adapter chains.

    Args:
        gh: NetworkX DiGraph representing the adapter connections

    Returns:
        Tuple containing:
        - Set of all possible adapter combinations (as tuples)
        - Count of unique combinations
    """
    if not gh:
        return set(), 0
    source = min(gh.nodes())
    target = max(gh.nodes())
    all_paths = set()
    for path in nx.all_simple_paths(gh, source=source, target=target):
        all_paths.add(tuple(path))
    return all_paths, len(all_paths)
