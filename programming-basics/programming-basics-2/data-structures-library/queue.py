# Queue Implementation

class Queue:
    """Implementation of a queue using a list"""
    
    def __init__(self):
        """Initialize an empty queue"""
        self.items = []
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add an item to the back of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items.pop(0)
    
    def peek(self):
        """Return the front item from the queue without removing it"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)


class LinkedQueue:
    """Implementation of a queue using a linked list"""
    
    def __init__(self):
        """Initialize an empty queue"""
        self.front = None
        self.rear = None
        self._size = 0
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None
    
    def enqueue(self, item):
        """Add an item to the back of the queue"""
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item
    
    def peek(self):
        """Return the front item from the queue without removing it"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.front.data
    
    def size(self):
        """Return the number of items in the queue"""
        return self._size


class ArrayQueue:
    """Implementation of a queue using a circular array"""
    
    def __init__(self, capacity=10):
        """Initialize an empty queue with the given capacity"""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self._size == 0
    
    def enqueue(self, item):
        """Add an item to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = item
        self._size += 1
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result
    
    def peek(self):
        """Return the front item from the queue without removing it"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]
    
    def size(self):
        """Return the number of items in the queue"""
        return self._size
    
    def _resize(self, capacity):
        """Resize the array to the given capacity"""
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
