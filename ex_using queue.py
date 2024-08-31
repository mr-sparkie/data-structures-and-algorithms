#use a delivery handler
import time
from threading import *
from queue import Queue
q1 = Queue()
class place_order(Thread):
    def __init__(self):
        self.q1 = q1


    def place(self,order):
        self.q1.enqueue(order)
        print("your order\t" + order + "\tdelivered soon")

class serve_order(Thread):
    def __init__(self):
        self.q1 = q1
    def serve(self):
        time.sleep(2)
        print("take your \t"+self.q1.dequeue()+"\tsir")
c1 = place_order()
c2 = serve_order()
n = ["pizza","dosa","burger","nuggets","fries"]
for i in n:
    c1.place(i)
    time.sleep(0.5)
    c2.serve()
    time.sleep(1)