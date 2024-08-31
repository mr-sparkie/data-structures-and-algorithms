from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,val):
        self.queue.appendleft(val)
    def dequeue(self):
        return self.queue.pop()
    def disp(self):
        print(self.queue)
    def is_empty(self):
        print(len(self.queue)==0)
    def size(self):
        print(len(self.queue))
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.dequeue()
# q.dequeue()
# q.disp()