"""
LeetCode Q232: Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions 
of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.
"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x: int) -> None:
        self.stack1.append(x)
    
    def pop(self) -> int:
        self._move()
        return self.stack2.pop()
    
    def peek(self) -> int:
        self._move()
        return self.stack2[-1]
    
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def _move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

