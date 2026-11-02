# Stack Implementation

class Stack:
    """Implementation of a stack using a list"""
    
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self.items == []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item from the stack without removing it"""
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[len(self.items)-1]
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __iter__(self):
        """Return an iterator for the stack"""
        for item in reversed(self.items):
            yield item


class LinkedStack:
    """Implementation of a stack using a linked list"""
    
    def __init__(self):
        """Initialize an empty stack"""
        self._top = None
        self._size = 0
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self._top is None
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self._top = Node(item, self._top)
        self._size += 1
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise ValueError("Stack is empty")
        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        return item
    
    def peek(self):
        """Return the top item from the stack without removing it"""
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._top.data
    
    def size(self):
        """Return the number of items in the stack"""
        return self._size
    
    def __iter__(self):
        """Return an iterator for the stack"""
        def _iter_helper(node):
            if node is not None:
                _iter_helper(node.next)
                yield node.data
        
        return _iter_helper(self._top)


def check_balanced_parentheses(expression):
    """Check if parentheses, brackets, and braces in an expression are balanced"""
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """Evaluate a postfix expression using a stack"""
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        if token in "+-*/":
            # It's an operator, pop two operands
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            # It's an operand, push onto stack
            stack.push(float(token))
    
    # The final result should be the only item on the stack
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()
