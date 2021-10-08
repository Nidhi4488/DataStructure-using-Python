#Approaches in python :list,collections.deque
#using List
from collections import deque
queue=[]
queue.insert(0,24)
queue.insert(0,25)
queue.insert(0,26)
queue.insert(0,27)
print(queue)
print(queue.pop())
print(queue)

#using deque
#append(x) incase of stack appendleft(x) incase of queue
queue2=deque()
queue2.appendleft(1)
queue2.appendleft(2)
queue2.appendleft(3)
queue2.appendleft(4)
print(queue2)
queue2.pop()
print(queue2)

#Implementing using class
class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,value):
        self.buffer.appendleft(value)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    def display(self):
        s=[]
        for i in self.buffer:
            s.append(i)

        print(s)

q=Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
q.buffer


#3rd method
from queue import Queue

queue3=Queue(maxsize=3)
print(queue3.qsize())
queue3.put(2)
queue3.put(3)
queue3.put(4)
print(queue3.full())
print(queue3.get())
print(queue3.get())
print(queue3.get())
print(queue3.empty())











