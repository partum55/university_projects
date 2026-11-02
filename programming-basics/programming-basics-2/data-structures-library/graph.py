# Graph Implementation

class Vertex:
    """Lightweight vertex structure for a graph"""
    
    def __init__(self, label=None):
        """Initialize a vertex, optionally with a label"""
        self._label = label
        self._marked = False
    
    def is_marked(self):
        """Return True if the vertex is marked"""
        return self._marked
    
    def set_mark(self):
        """Set the vertex mark to True"""
        self._marked = True
    
    def clear_mark(self):
        """Set the vertex mark to False"""
        self._marked = False
    
    def get_label(self):
        """Return the label associated with this vertex"""
        return self._label
    
    def set_label(self, label):
        """Set the label associated with this vertex"""
        self._label = label
    
    def __eq__(self, other):
        """Two vertices are equal if they have the same labels"""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._label == other._label
    
    def __hash__(self):
        """Vertex hash method needed for dictionary keys"""
        return hash(self._label)
    
    def __str__(self):
        """String representation of the vertex"""
        return str(self._label)


class Edge:
    """Lightweight edge structure for a graph"""
    
    def __init__(self, source, target, weight=None):
        """Initialize an edge from source to target with optional weight"""
        self._source = source
        self._target = target
        self._weight = weight  # weight is optional
        self._marked = False
    
    def is_marked(self):
        """Return True if the edge is marked"""
        return self._marked
    
    def set_mark(self):
        """Set the edge mark to True"""
        self._marked = True
    
    def clear_mark(self):
        """Set the edge mark to False"""
        self._marked = False
    
    def get_source(self):
        """Return the source vertex of this edge"""
        return self._source
    
    def get_target(self):
        """Return the target vertex of this edge"""
        return self._target
    
    def get_weight(self):
        """Return the weight associated with this edge"""
        return self._weight
    
    def set_weight(self, weight):
        """Set the weight associated with this edge"""
        self._weight = weight
    
    def __eq__(self, other):
        """Two edges are equal if they connect the same vertices"""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._source == other._source and                self._target == other._target
    
    def __hash__(self):
        """Edge hash method needed for dictionary keys"""
        return hash((self._source, self._target))
    
    def __str__(self):
        """String representation of the edge"""
        result = str(self._source) + ">" + str(self._target)
        if self._weight is not None:
            result += ":" + str(self._weight)
        return result


class LinkedDirectedGraph:
    """A graph implemented with an adjacency list"""
    
    def __init__(self):
        """Create an empty graph"""
        self._vertices = {}  # Maps vertex labels to vertex objects
        self._edges = {}     # Maps vertex labels to dictionary of incident edges
    
    def __str__(self):
        """Returns the string representation of the graph"""
        result = str(len(self._vertices)) + " Vertices: "
        for vertex in self._vertices.values():
            result += str(vertex) + " "
        result += "\n"
        result += str(self.edge_count()) + " Edges: "
        for edge in self.get_edges():
            result += str(edge) + " "
        return result
    
    def clear_marks(self):
        """Clear all vertex and edge marks"""
        for vertex in self._vertices.values():
            vertex.clear_mark()
        for edges in self._edges.values():
            for edge in edges.values():
                edge.clear_mark()
    
    def clear_vertex_marks(self):
        """Clear all vertex marks"""
        for vertex in self._vertices.values():
            vertex.clear_mark()
    
    def clear_edge_marks(self):
        """Clear all edge marks"""
        for edges in self._edges.values():
            for edge in edges.values():
                edge.clear_mark()
    
    def add_vertex(self, label):
        """Add a vertex with the given label to the graph"""
        if label not in self._vertices:
            self._vertices[label] = Vertex(label)
            self._edges[label] = {}
        return self._vertices[label]
    
    def remove_vertex(self, label):
        """Remove a vertex with the given label from the graph"""
        if label in self._vertices:
            # Remove all edges connected to this vertex
            for target_label in list(self._edges.keys()):
                if label in self._edges[target_label]:
                    del self._edges[target_label][label]
            
            # Remove the vertex and its outgoing edges
            del self._vertices[label]
            del self._edges[label]
    
    def add_edge(self, source_label, target_label, weight=None):
        """Add an edge from the source vertex to the target vertex"""
        # Add the vertices if they don't exist
        if source_label not in self._vertices:
            self.add_vertex(source_label)
        if target_label not in self._vertices:
            self.add_vertex(target_label)
        
        # Add the edge
        self._edges[source_label][target_label] = Edge(
            self._vertices[source_label],
            self._vertices[target_label],
            weight
        )
    
    def remove_edge(self, source_label, target_label):
        """Remove an edge from the source vertex to the target vertex"""
        if source_label in self._edges and target_label in self._edges[source_label]:
            del self._edges[source_label][target_label]
    
    def get_edge(self, source_label, target_label):
        """Return the edge from the source vertex to the target vertex"""
        if source_label in self._edges and target_label in self._edges[source_label]:
            return self._edges[source_label][target_label]
        return None
    
    def get_vertex(self, label):
        """Return the vertex with the given label"""
        if label in self._vertices:
            return self._vertices[label]
        return None
    
    def get_vertices(self):
        """Return an iterator over all vertices in the graph"""
        return iter(self._vertices.values())
    
    def get_edges(self):
        """Return an iterator over all edges in the graph"""
        edges = []
        for source_edges in self._edges.values():
            edges.extend(source_edges.values())
        return iter(edges)
    
    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._vertices)
    
    def edge_count(self):
        """Return the number of edges in the graph"""
        count = 0
        for source_edges in self._edges.values():
            count += len(source_edges)
        return count
    
    def neighboring_vertices(self, label):
        """Return an iterator over the neighboring vertices of the vertex with the given label"""
        if label in self._edges:
            return iter([self._vertices[target_label] for target_label in self._edges[label]])
        return iter([])
    
    def incident_edges(self, label):
        """Return an iterator over all incident edges of the vertex with the given label"""
        if label in self._edges:
            return iter(self._edges[label].values())
        return iter([])
    
    def is_adjacent(self, source_label, target_label):
        """Return True if the vertices with the given labels are adjacent"""
        return source_label in self._edges and target_label in self._edges[source_label]
