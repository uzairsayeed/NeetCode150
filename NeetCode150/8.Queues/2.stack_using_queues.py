# Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 

# Follow-up: Can you implement the stack using only one queue?

from collections import deque
class MyStack:
    # Day-01: 17/Aug/2026
    # Recognition Pattern: q1 always contains the current stack elements in insertion order; q2 is just temporary storage used during pop.
    # Pattern: Two Queues
    # Intuition:
        # push(x)
            # → append to q1
        # pop()
            # → move q1 elements to q2 until only one remains
            # → remove the final q1 element (this is stack top)
            # → swap q1 and q2
        # top()
            # → similar idea, but preserve the last element instead of permanently removing it
            #   -> move all but the last q1 element to q2
            #   -> temporarily remove the last element
            #   -> append it to q2 so it remains in the stack
            #   -> swap q1 and q2
        # empty()
            # → q1 is empty
    # TC:
        # push  -> O(1)
        # pop   -> O(n)
        # top   -> O(n)
        # empty -> O(1)
    # SC = O(n)
    # Mistakes MAde:
        # Missed the swapping logic, during the pop()
        # Rating: 3/5
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
       
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        popped_element = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())

        top_element = self.q1.popleft()
        self.q2.append(top_element)

        self.q1, self.q2 = self.q2, self.q1

        return top_element
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
