# Exercise 13: Stack Implementation
# Implement a stack data structure with push, pop, and peek operations.
# Example: push 1, push 2, peek should return 2, pop should return 2

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Test the stack
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())  # Expected: 2
    print(stack.pop())   # Expected: 2
    print(stack.pop())   # Expected: 1
    print(stack.is_empty())  # Expected: True
