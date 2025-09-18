# Exercise 14: Queue Implementation
# Implement a queue data structure with enqueue, dequeue, and front operations.
# Example: enqueue 1, enqueue 2, front should return 1, dequeue should return 1

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Test the queue
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.front())  # Expected: 1
    print(queue.dequeue())  # Expected: 1
    print(queue.dequeue())  # Expected: 2
    print(queue.is_empty())  # Expected: True
