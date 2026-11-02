# Node Implementation for Linked Structures

class Node:
    """Base class for nodes in linked data structures"""
    
    def __init__(self, data=None, next=None):
        """Initialize a new node with data and next reference"""
        self.data = data
        self.next = next
    
    def __str__(self):
        """Return string representation of node data"""
        return str(self.data)
