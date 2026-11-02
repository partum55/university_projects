# Graph Algorithms

from queue import Queue
from stack import Stack


# Depth-First Search
def dfs(graph, start_vertex, process=print):
    """Perform a depth-first search traversal of the graph starting from start_vertex"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Helper function for recursive DFS
    def dfs_helper(vertex):
        # Process the current vertex
        process(vertex)
        vertex.set_mark()  # Mark as visited
        
        # Visit all unvisited neighbors
        for neighbor in graph.neighboring_vertices(vertex.get_label()):
            if not neighbor.is_marked():
                dfs_helper(neighbor)
    
    # Start DFS from the start vertex
    start = graph.get_vertex(start_vertex)
    if start:
        dfs_helper(start)


def dfs_iterative(graph, start_vertex, process=print):
    """Perform a depth-first search traversal using a stack"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Create a stack for DFS
    stack = Stack()
    start = graph.get_vertex(start_vertex)
    if not start:
        return
    
    # Push the starting vertex
    stack.push(start)
    
    while not stack.is_empty():
        # Pop a vertex from stack
        vertex = stack.pop()
        
        # If the vertex is not visited yet
        if not vertex.is_marked():
            # Process the vertex
            process(vertex)
            vertex.set_mark()  # Mark as visited
            
            # Push all unvisited neighbors to stack
            for neighbor in graph.neighboring_vertices(vertex.get_label()):
                if not neighbor.is_marked():
                    stack.push(neighbor)


def dfs_complete(graph, process=print):
    """Perform a complete DFS traversal visiting all vertices"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Traverse each unvisited vertex
    for vertex in graph.get_vertices():
        if not vertex.is_marked():
            dfs(graph, vertex.get_label(), process)


# Breadth-First Search
def bfs(graph, start_vertex, process=print):
    """Perform a breadth-first search traversal"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Create a queue for BFS
    queue = Queue()
    start = graph.get_vertex(start_vertex)
    if not start:
        return
    
    # Mark the source vertex as visited and enqueue it
    start.set_mark()
    queue.put(start)
    
    while not queue.empty():
        # Dequeue a vertex from queue
        vertex = queue.get()
        
        # Process the vertex
        process(vertex)
        
        # Get all adjacent vertices of the dequeued vertex
        # If adjacent is not visited, then mark it visited and enqueue it
        for neighbor in graph.neighboring_vertices(vertex.get_label()):
            if not neighbor.is_marked():
                neighbor.set_mark()
                queue.put(neighbor)


def bfs_complete(graph, process=print):
    """Perform a complete BFS traversal of the graph"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Traverse each unvisited vertex
    for vertex in graph.get_vertices():
        if not vertex.is_marked():
            bfs(graph, vertex.get_label(), process)


# Topological Sort
def topological_sort_kahn(graph):
    """Perform a topological sort using Kahn's algorithm"""
    # Create a dictionary to store in-degrees of all vertices
    in_degree = {vertex.get_label(): 0 for vertex in graph.get_vertices()}
    
    # Calculate in-degrees for all vertices
    for edge in graph.get_edges():
        target_label = edge.get_target().get_label()
        in_degree[target_label] += 1
    
    # Create a queue and enqueue all vertices with in-degree 0
    queue = Queue()
    for vertex in graph.get_vertices():
        if in_degree[vertex.get_label()] == 0:
            queue.put(vertex)
    
    # Initialize result list
    topo_order = []
    
    # Process vertices in the queue
    while not queue.empty():
        vertex = queue.get()
        topo_order.append(vertex.get_label())
        
        # Decrease in-degree of adjacent vertices
        for neighbor in graph.neighboring_vertices(vertex.get_label()):
            neighbor_label = neighbor.get_label()
            in_degree[neighbor_label] -= 1
            
            # If in-degree becomes 0, add to queue
            if in_degree[neighbor_label] == 0:
                queue.put(neighbor)
    
    # If not all vertices are included, there's a cycle
    if len(topo_order) != graph.vertex_count():
        return None
    
    return topo_order


def topological_sort_dfs(graph):
    """Perform a topological sort using DFS"""
    # Mark all vertices as unvisited
    graph.clear_vertex_marks()
    
    # Stack to store the topological order
    stack = Stack()
    
    # To track if the graph has a cycle
    visiting = set()
    visited = set()
    
    def dfs_topological_sort(vertex):
        """Helper function for DFS-based topological sort"""
        label = vertex.get_label()
        
        # If vertex is currently being visited, there's a cycle
        if label in visiting:
            return False
        
        # If vertex is already visited, skip
        if label in visited:
            return True
        
        # Mark vertex as being visited
        visiting.add(label)
        
        # Visit all neighbors
        for neighbor in graph.neighboring_vertices(label):
            if not dfs_topological_sort(neighbor):
                return False
        
        # Remove from visiting set and add to visited set
        visiting.remove(label)
        visited.add(label)
        
        # Add to stack
        stack.push(label)
        
        return True
    
    # Visit all vertices
    for vertex in graph.get_vertices():
        if vertex.get_label() not in visited:
            if not dfs_topological_sort(vertex):
                return None  # Graph has a cycle
    
    # Convert stack to list (reverse order)
    topo_order = []
    while not stack.is_empty():
        topo_order.append(stack.pop())
    
    return topo_order


# Shortest Path Algorithms
def dijkstra_shortest_path(graph, start_vertex):
    """Find the shortest path from start_vertex to all other vertices"""
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex.get_label(): float('inf') for vertex in graph.get_vertices()}
    distances[start_vertex] = 0
    
    # Dictionary to store the predecessor of each vertex in the shortest path
    predecessors = {vertex.get_label(): None for vertex in graph.get_vertices()}
    
    # Set of unvisited vertices
    unvisited = set(vertex.get_label() for vertex in graph.get_vertices())
    
    # While there are still unvisited vertices
    while unvisited:
        # Find the unvisited vertex with the smallest distance
        current = min(unvisited, key=lambda v: distances[v])
        
        # If the smallest distance is infinity, the remaining vertices are not reachable
        if distances[current] == float('inf'):
            break
        
        # Remove the current vertex from the unvisited set
        unvisited.remove(current)
        
        # Update distances to all neighboring vertices
        for edge in graph.incident_edges(current):
            neighbor = edge.get_target().get_label()
            weight = edge.get_weight()
            
            if weight is None:  # Skip unweighted edges
                continue
            
            # Calculate new distance
            new_distance = distances[current] + weight
            
            # If the new distance is shorter than the current distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current
    
    return distances, predecessors


def bellman_ford_shortest_path(graph, start_vertex):
    """Find the shortest path from start_vertex to all other vertices"""
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex.get_label(): float('inf') for vertex in graph.get_vertices()}
    distances[start_vertex] = 0
    
    # Dictionary to store the predecessor of each vertex in the shortest path
    predecessors = {vertex.get_label(): None for vertex in graph.get_vertices()}
    
    # Relax edges repeatedly
    vertex_count = graph.vertex_count()
    
    # Perform |V|-1 relaxations
    for _ in range(vertex_count - 1):
        # Relax all edges
        for edge in graph.get_edges():
            source = edge.get_source().get_label()
            target = edge.get_target().get_label()
            weight = edge.get_weight()
            
            if weight is None:  # Skip unweighted edges
                continue
            
            # Relaxation step
            if distances[source] != float('inf') and distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight
                predecessors[target] = source
    
    # Check for negative cycles
    has_negative_cycle = False
    for edge in graph.get_edges():
        source = edge.get_source().get_label()
        target = edge.get_target().get_label()
        weight = edge.get_weight()
        
        if weight is None:  # Skip unweighted edges
            continue
        
        # If we can still relax an edge, there's a negative cycle
        if distances[source] != float('inf') and distances[source] + weight < distances[target]:
            has_negative_cycle = True
            break
    
    return distances, predecessors, has_negative_cycle


def floyd_warshall_all_pairs_shortest_paths(graph):
    """Find the shortest paths between all pairs of vertices"""
    # Get all vertex labels
    vertices = [v.get_label() for v in graph.get_vertices()]
    n = len(vertices)
    
    # Initialize distances and next_vertex matrices
    distances = {}
    next_vertex = {}
    
    # Initialize distances with infinity
    for u in vertices:
        for v in vertices:
            distances[(u, v)] = float('inf')
            next_vertex[(u, v)] = None
    
    # Distance from a vertex to itself is 0
    for v in vertices:
        distances[(v, v)] = 0
    
    # Initialize direct edge weights
    for edge in graph.get_edges():
        u = edge.get_source().get_label()
        v = edge.get_target().get_label()
        weight = edge.get_weight()
        
        if weight is not None:
            distances[(u, v)] = weight
            next_vertex[(u, v)] = v
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[(i, k)] + distances[(k, j)] < distances[(i, j)]:
                    distances[(i, j)] = distances[(i, k)] + distances[(k, j)]
                    next_vertex[(i, j)] = next_vertex[(i, k)]
    
    # Check for negative cycles
    has_negative_cycle = False
    for v in vertices:
        if distances[(v, v)] < 0:
            has_negative_cycle = True
            break
    
    return distances, next_vertex, has_negative_cycle


# Minimum Spanning Tree Algorithms
def prim_minimum_spanning_tree(graph):
    """Find a minimum spanning tree using Prim's algorithm"""
    # Get all vertices
    vertices = list(graph.get_vertices())
    if not vertices:
        return set()
    
    # Start with any vertex
    start = vertices[0].get_label()
    
    # Set of vertices included in MST
    included = {start}
    
    # Set of edges in the MST
    mst_edges = set()
    
    # While not all vertices are included
    while len(included) < len(vertices):
        min_edge = None
        min_weight = float('inf')
        
        # Find the minimum weight edge connecting an included vertex to an unincluded vertex
        for u in included:
            for edge in graph.incident_edges(u):
                v = edge.get_target().get_label()
                weight = edge.get_weight()
                
                if v not in included and weight is not None and weight < min_weight:
                    min_edge = edge
                    min_weight = weight
        
        # If no edge found, graph is not connected
        if min_edge is None:
            break
        
        # Add the target vertex to included set
        included.add(min_edge.get_target().get_label())
        
        # Add the edge to MST
        mst_edges.add(min_edge)
    
    return mst_edges


def kruskal_minimum_spanning_tree(graph):
    """Find a minimum spanning tree using Kruskal's algorithm"""
    # Get all edges and sort them by weight
    edges = [(edge.get_weight(), edge) for edge in graph.get_edges() if edge.get_weight() is not None]
    edges.sort()
    
    # Initialize disjoint set for each vertex
    parent = {}
    rank = {}
    
    def make_set(vertex):
        parent[vertex] = vertex
        rank[vertex] = 0
    
    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]
    
    def union(vertex1, vertex2):
        root1 = find(vertex1)
        root2 = find(vertex2)
        
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    # Make a set for each vertex
    for vertex in graph.get_vertices():
        make_set(vertex.get_label())
    
    # Set of edges in the MST
    mst_edges = set()
    
    # Process edges in order of increasing weight
    for weight, edge in edges:
        u = edge.get_source().get_label()
        v = edge.get_target().get_label()
        
        # If including this edge doesn't create a cycle
        if find(u) != find(v):
            mst_edges.add(edge)
            union(u, v)
    
    return mst_edges
