# Deque (Double-Ended Queue) Implementation

class Deque:
    """Implementation of a deque using a list"""
    
    def __init__(self):
        """Initialize an empty deque"""
        self.items = []
    
    def is_empty(self):
        """Check if the deque is empty"""
        return len(self.items) == 0
    
    def add_front(self, item):
        """Add an item to the front of the deque"""
        self.items.insert(0, item)
    
    def add_rear(self, item):
        """Add an item to the back of the deque"""
        self.items.append(item)
    
    def remove_front(self):
        """Remove and return the front item from the deque"""
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items.pop(0)
    
    def remove_rear(self):
        """Remove and return the back item from the deque"""
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items.pop()
    
    def peek_front(self):
        """Return the front item from the deque without removing it"""
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items[0]
    
    def peek_rear(self):
        """Return the back item from the deque without removing it"""
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the deque"""
        return len(self.items)
