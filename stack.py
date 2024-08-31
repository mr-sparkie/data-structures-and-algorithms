from collections import deque
class stack:
    def __init__(self):
        self.stack = deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        print(self.stack.pop())
    def peek(self):
        print(self.stack[-1])
    def add_multiple(self,val):
        self.stack.extend(val)
    def empyt_list(self):
        self.stack.clear()
    def is_empyt(self):
        print(len(self.stack) == 0)
    def size(self):
        print(len(self.stack))
    def disp(self):
        print(self.stack)
s1 = stack()
s1.push(1)
s1.push(2)
s1.add_multiple([4,5,6])
# s1.empyt_list()
s1.peek()
s1.pop()
s1.peek()
s1.pop()
s1.size()
s1.disp()
