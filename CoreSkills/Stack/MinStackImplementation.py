###############################################
# Problem statement:
# https://leetcode.com/problems/min-stack/description/
###############################################

class MinStack:

    def __init__(self):
        # Initializing
        self.stack = []
        self._min = None
        
    def push(self, val: int) -> None:
        # Adding current val with current min val into the stack, it keep track of prior min val if current val got popped out
        self.stack.append([val, self._min])
        # If current val is less than the current min, then updating current min 
        if self._min is None or val < self._min:
            self._min = val

    def pop(self) -> None:
        # Poping out the last node from stack
        val = self.stack.pop()
        # Checking if current popped out value is min val or not, if yes, then reassign curr min val to prior min value
        if val[0] == self._min:
            self._min = val[-1]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self._min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()