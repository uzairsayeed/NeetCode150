# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, 
# which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. 
# You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
 

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? 
# In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.




class MyQueue:
    # Day-01: 16/Aug/2026
    # Recognition Pattern: s1 stores newly arrived elements; s2 stores elements in queue-removal order. Transfer only when s2 is empty.
    # Pattern: Two Stacks
    # Intuition:
        # push(x)
            # → always push to s1
        # pop()
            # → if s2 has elements, pop s2
            # → if s2 is empty, move everything s1 → s2, then pop s2
        # peek()
            # If s2 is not empty -> return s2[-1]
            # else transfer all the elments from s1 to s2 -> return s2[-1]
        # empty()
            # if BOTH s1 and s2 are empty, return True
            # otherwise return False
    # TC:
        # push  → O(1)
        # peek  → O(1) amortized
        # pop   → O(1) amortized
        # empty → O(1)
    # SC: O(n)
    # Mistakes Made:
        # Initially thought of transferring elements back from s2 -> s1 after pop.
        # Missed the optimization that s2 should retain elements in FIFO-removal order.
        # Rating: 3/5
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()

    def peek(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        return self.stack_2[-1]

    def empty(self) -> bool:
        return not self.stack_1 and not self.stack_2        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
obj.push(4)
obj.push(6)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
