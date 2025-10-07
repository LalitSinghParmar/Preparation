###############################################
# Problem Statement:
# https://leetcode.com/problems/implement-stack-using-queues/description/
###############################################
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        # first append element in the end 
        self.queue.append(x)
        # Poping element from left and adding in end so that our element x will be in front, which will support pop from front
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()