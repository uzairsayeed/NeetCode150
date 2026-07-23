# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


class MinStack1:
    # Approach-1:
        # Issue 1: remove() is O(n). Python's list.remove(x) searches the list to find x.
        # Issue 2: Push isn't O(1)

    def __init__(self):
        self.min_stack = []
        self.min_values = [float('inf')]

        

    def push(self, value: int) -> None:
        pops_needed = 0
        while self.min_values and (self.min_values[-1]) < value:
            popped_element = self.min_values.pop()
            self.min_stack.append(popped_element)
            pops_needed += 1

        self.min_values.append(value)

        while pops_needed:
            self.min_values.append(self.min_stack.pop())
            pops_needed -= 1
            
        self.min_stack.append(value)
        
    def pop(self) -> None:
        popped_element = self.min_stack.pop()
        self.min_values.remove(popped_element)

        

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
        
class MinStack:
    # Day-0: 23/July/2026
    # Recognition Trigger : History of min values
    # Intuition:
        # Maintain an auxiliary stack that mirrors the main stack. At every depth, it stores the minimum element seen up to that point. 
        # Thus, every stack state remembers its minimum, making getMin() an O(1) lookup.
    # Mistakes Made:
        # Instead of maintaining the history I was maintaining a sorted stack
    # NOTE: Mirror the main stack with a min-stack that stores the minimum at every stack state. 
        # This preserves the history of minimums, allowing getMin() in O(1).
    def __init__(self):
        self.min_stack = []
        self.min_values = []

    def push(self, value: int) -> None:
        # The idea here is, the min_values will hold the curr min value of the stack as per its curr state.
        # So we're just maintaining the hisotry of min values at each step
        if self.min_values:
            curr_min = min(self.min_values[-1], value)
        else:
            curr_min = value
        self.min_values.append(curr_min)
        self.min_stack.append(value)

        
    def pop(self) -> None:
        self.min_stack.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())


