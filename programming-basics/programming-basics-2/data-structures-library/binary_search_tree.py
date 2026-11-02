# Binary Search Tree Implementation

class BSTNode:
    """Lightweight class for storing BST nodes"""
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkedBST:
    """Linked Binary Search Tree implementation"""
    
    def __init__(self):
        """Initialize an empty binary search tree"""
        self._root = None
        self._size = 0
    
    def __len__(self):
        """Return the number of items in the tree"""
        return self._size
    
    def is_empty(self):
        """Check if the tree is empty"""
        return len(self) == 0
    
    def __contains__(self, item):
        """Return True if item is in the tree"""
        return self._contains(self._root, item)
    
    def _contains(self, node, item):
        """Helper method for __contains__"""
        if node is None:
            return False
        elif item == node.data:
            return True
        elif item < node.data:
            return self._contains(node.left, item)
        else:
            return self._contains(node.right, item)
    
    def find(self, item):
        """Return item if found or None if not found"""
        return self._find(self._root, item)
    
    def _find(self, node, item):
        """Helper method for find"""
        if node is None:
            return None
        elif item == node.data:
            return node.data
        elif item < node.data:
            return self._find(node.left, item)
        else:
            return self._find(node.right, item)
    
    def add(self, item):
        """Add item to the tree"""
        if self.is_empty():
            self._root = BSTNode(item)
        else:
            self._add(self._root, item)
        self._size += 1
    
    def _add(self, node, item):
        """Helper method to add item to BST"""
        if item < node.data:
            if node.left is None:
                node.left = BSTNode(item)
            else:
                self._add(node.left, item)
        else:
            if node.right is None:
                node.right = BSTNode(item)
            else:
                self._add(node.right, item)
    
    def remove(self, item):
        """Remove item from the tree and return it if found, otherwise None"""
        if self.is_empty():
            return None
        else:
            removed_item = self.find(item)
            if removed_item:
                self._root = self._remove(self._root, item)
                self._size -= 1
            return removed_item
    
    def _remove(self, node, item):
        """Helper method to remove item from BST"""
        if node is None:
            return None
        elif item < node.data:
            node.left = self._remove(node.left, item)
            return node
        elif item > node.data:
            node.right = self._remove(node.right, item)
            return node
        else:  # item == node.data
            if node.left is None and node.right is None:  # Leaf node
                return None
            elif node.left is None:  # One right child
                return node.right
            elif node.right is None:  # One left child
                return node.left
            else:  # Two children
                # Find successor (smallest item in right subtree)
                successor = self._find_min(node.right)
                node.data = successor  # Replace with successor
                node.right = self._remove(node.right, successor)  # Remove successor
                return node
    
    def _find_min(self, node):
        """Find minimum value in subtree rooted at node"""
        current = node
        while current.left is not None:
            current = current.left
        return current.data
    
    def inorder(self):
        """Generate an inorder iteration of items in the tree"""
        return self._inorder(self._root)
    
    def _inorder(self, node):
        """Helper method for inorder traversal"""
        items = []
        def recurse(node):
            if node is not None:
                recurse(node.left)
                items.append(node.data)
                recurse(node.right)
        recurse(node)
        return iter(items)
    
    def preorder(self):
        """Generate a preorder iteration of items in the tree"""
        return self._preorder(self._root)
    
    def _preorder(self, node):
        """Helper method for preorder traversal"""
        items = []
        def recurse(node):
            if node is not None:
                items.append(node.data)
                recurse(node.left)
                recurse(node.right)
        recurse(node)
        return iter(items)
    
    def postorder(self):
        """Generate a postorder iteration of items in the tree"""
        return self._postorder(self._root)
    
    def _postorder(self, node):
        """Helper method for postorder traversal"""
        items = []
        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                items.append(node.data)
        recurse(node)
        return iter(items)
    
    def __iter__(self):
        """Generate an inorder iteration of items in the tree"""
        return self.inorder()
