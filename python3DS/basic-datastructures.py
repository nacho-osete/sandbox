"""
   Some basic data structures and 
   their classes, as long as they
   don't come along as built-in 
   data types with Python.

   Optionally, you can use the PYTHONDS3
   library (pip installable). More details 
   just in the code listing.

   - Stacks
   - Queues

"""

class Stack_basic:
    """Stack basic implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

# Alternative implementation from the pythonds3 library
# -> sudo pip3 install pythonds3
from pythonds3.basic import Stack

s = Stack()

print(s.is_empty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

m = Stack()
m.push("x")
m.push("y")
m.push("z")

while not m.is_empty(): 
    print(m.peek())
    m.pop()

q = Queue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q.size())
q.enqueue(8.4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
