# Examples of using data structures and algorithms
from stack import Stack, check_balanced_parentheses, evaluate_postfix
from queue import Queue
from binary_search_tree import LinkedBST
from graph import LinkedDirectedGraph
from graph_algorithms import (dfs, bfs, topological_sort_kahn, 
                              dijkstra_shortest_path, kruskal_minimum_spanning_tree)
from sorting_algorithms import (bubble_sort, selection_sort, insertion_sort, 
                              merge_sort, quick_sort, heap_sort, counting_sort)
from point import Point
from church import Church


# Binary Search Tree Example: Find kth smallest element
def find_kth_smallest(bst, k):
    """Find the kth smallest element in a BST."""
    if k <= 0 or k > len(bst):
        return None
    
    # Inorder traversal gives elements in sorted order
    elements = []
    for element in bst.inorder():
        elements.append(element)
        if len(elements) == k:
            return elements[-1]
    
    return None


# Graph Example: Find shortest path
def find_shortest_path(graph, start, end):
    """Find the shortest path between start and end vertices in a graph."""
    # Run Dijkstra's algorithm
    distances, predecessors = dijkstra_shortest_path(graph, start)
    
    # If end is not reachable
    if distances[end] == float('inf'):
        return None
    
    # Reconstruct the path
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    # Reverse the path to get start to end
    path.reverse()
    
    return path


# Demo function to run all examples
def run_examples():
    print("Running examples of data structures and algorithms...")
    
    print("\n1. Point Class Example")
    point1 = Point(3, 4)
    point2 = Point(1, 1)
    print(f"Point 1: {point1}")
    print(f"Point 2: {point2}")
    point1.rotate(90, point2)
    print(f"Point 1 after rotation around point 2: {point1}")
    
    print("\n2. Church Class Example")
    church = Church("St. Michael's", 1865, "Lviv", "wood")
    print(church)
    print(f"Age of church: {church.get_age(2023)} years")
    
    print("\n3. Stack Example: Check balanced parentheses")
    print(f"'([])' is balanced: {check_balanced_parentheses('([])')}")
    print(f"'({[]})' is balanced: {check_balanced_parentheses('({[]})')}")
    print(f"'({[]}' is balanced: {check_balanced_parentheses('({[]}')}")
    
    print("\n4. Stack Example: Evaluate postfix expression")
    print(f"'5 3 + 2 *' evaluates to: {evaluate_postfix('5 3 + 2 *')}")
    
    print("\n5. Binary Search Tree Example")
    bst = LinkedBST()
    for item in [50, 30, 70, 20, 40, 60, 80]:
        bst.add(item)
    print(f"BST elements in order: {list(bst.inorder())}")
    print(f"3rd smallest element: {find_kth_smallest(bst, 3)}")
    
    print("\n6. Graph Example")
    graph = LinkedDirectedGraph()
    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5), 
             ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2), ('D', 'F', 6), 
             ('E', 'F', 3)]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    
    print("Graph created with vertices: A, B, C, D, E, F")
    print(f"Shortest path from A to F: {find_shortest_path(graph, 'A', 'F')}")
    
    print("\n7. Sorting Algorithms Example")
    test_array = [5, 2, 9, 1, 5, 6]
    print(f"Original array: {test_array}")
    print(f"Bubble Sort:    {bubble_sort(test_array)}")
    print(f"Selection Sort: {selection_sort(test_array)}")
    print(f"Insertion Sort: {insertion_sort(test_array)}")
    print(f"Merge Sort:     {merge_sort(test_array)}")
    print(f"Quick Sort:     {quick_sort(test_array)}")
    print(f"Heap Sort:      {heap_sort(test_array)}")
    print(f"Counting Sort:  {counting_sort(test_array)}")
    
    print("\nAll examples completed!")


if __name__ == "__main__":
    run_examples()
