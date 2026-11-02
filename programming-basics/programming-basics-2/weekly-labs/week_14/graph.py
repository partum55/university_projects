"""Temp"""


def read_file(filename: str) -> list:
    """
    Read file

    :param filename: string filename
    :return: list of values
    """
    with open(filename, 'r', encoding='utf-8') as file:
        values = sorted(int(i.strip()) for i in file)
        if 0 not in values:
            values = [0] + values
        device_voltage = max(values) + 3
        if device_voltage not in values:
            values.append(device_voltage)
        return sorted(values)


def create_graph(arr: list) -> dict:
    """
    Creates a directed graph where adapters can connect to
    other adapters with joltage difference of 1-3.

    Args:
        arr: List of joltages (sorted)

    Returns:
        Dictionary representing the graph where keys are joltages
        and values are sets of joltages they can connect to
    """
    graph = {}
    for i in arr:
        graph[i] = set()
    for i, p in enumerate(arr):
        for j in range(i + 1, len(arr)):
            next_p = arr[j]
            diff = next_p - p
            if 1 <= diff <= 3:
                graph[p].add(next_p)
            elif diff > 3:
                break
    return graph


def find_combinations(graph: dict) -> (set, int):
    """
    Finds all possible combinations of adapters to connect from the outlet to the device.

    Args:
        graph: Dictionary representing the adapter graph where keys are joltages
               and values are sets of joltages they can connect to

    Returns:
        Tuple containing:
        - Set of all possible adapter combinations (as tuples)
        - Count of unique combinations
    """
    if not graph:
        return set(), 0
    min_joltage = min(graph.keys())
    max_joltage = max(graph.keys())
    all_paths = set()

    def dfs(current, path):
        if current == max_joltage:
            all_paths.add(tuple(path))
            return
        for next_adapter in graph[current]:
            dfs(next_adapter, path + [next_adapter])

    dfs(min_joltage, [min_joltage])
    return all_paths, len(all_paths)
