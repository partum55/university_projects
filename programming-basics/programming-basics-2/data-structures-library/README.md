# Data Structures and Algorithms Library

A comprehensive collection of data structures and algorithms implemented in Python. This library provides clean, well-documented implementations that can be used for educational purposes or as building blocks in larger projects.

## Table of Contents

- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Helper Classes](#helper-classes)
- [Examples](#examples)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Data Structures

The library includes the following data structures:

### Binary Trees

- **Binary Tree** (`binary_tree.py`): Abstract base class and linked implementation of a binary tree.
- **Binary Search Tree** (`binary_search_tree.py`): Implementation of a binary search tree with standard operations.

### Linear Structures

- **Stack** (`stack.py`): Array-based and linked list implementations of a stack.
- **Queue** (`queue.py`): Array-based, linked list, and circular array implementations of a queue.
- **Deque** (`deque.py`): Implementation of a double-ended queue.

### Graph

- **Graph** (`graph.py`): Implementation of a directed graph with adjacency list representation.

## Algorithms

### Graph Algorithms

The library includes various graph algorithms in `graph_algorithms.py`:

- **Traversal Algorithms**:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
- **Path Finding Algorithms**:
  - Dijkstra's Algorithm
  - Bellman-Ford Algorithm
  - Floyd-Warshall Algorithm
- **Other Graph Algorithms**:
  - Topological Sort (Kahn's Algorithm and DFS-based)
  - Minimum Spanning Tree (Prim's and Kruskal's Algorithms)

### Sorting Algorithms

The library includes various sorting algorithms in `sorting_algorithms.py`:

- **Comparison-Based Algorithms**:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
  - Shell Sort
- **Non-Comparison Algorithms**:
  - Counting Sort
  - Radix Sort

## Helper Classes

- **Node** (`node.py`): Base class for nodes in linked data structures.
- **Point** (`point.py`): Class for representing points in 2D space with operations.
- **Church** (`church.py`): Example class for representing churches in a database.

## Examples

The `examples.py` file provides examples of using the data structures and algorithms:

- Finding the kth smallest element in a binary search tree
- Finding the shortest path in a graph
- Demonstrating various sorting algorithms
- Using the Point and Church classes

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/partum55/university_projects.git
cd university_projects/programming-basics/programming-basics-2/data-structures-library
```

## Usage

You can import and use the data structures and algorithms in your Python code:

```python
# Import the required classes and functions
from stack import Stack
from queue import Queue
from binary_search_tree import LinkedBST
from sorting_algorithms import quick_sort

# Use the stack
stack = Stack()
stack.push(1)
stack.push(2)
item = stack.pop()  # Returns 2

# Use the binary search tree
bst = LinkedBST()
bst.add(5)
bst.add(3)
bst.add(7)
for item in bst.inorder():
    print(item)  # Prints 3, 5, 7

# Use a sorting algorithm
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = quick_sort(arr)  # Returns [1, 2, 5, 5, 6, 9]
```

For more examples, see the `examples.py` file.

## License

This project is licensed under the Mozilla Public License Version 2.0 - see the [LICENSE](LICENSE) file for details.
