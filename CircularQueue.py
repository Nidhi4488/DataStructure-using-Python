class CQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1

    def enqueue(self,value):
        #queue is full
        if ((self.rear+1)%self.size==self.front):
            print("Queue is full")
        elif (self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=value
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=value

    def dequeue(self):
        if (self.front == -1 and self.rear == -1):
            print("Queue is empty")
        elif(self.front==self.rear):
            # temp=self.queue[self.front]
            self.front=self.rear=-1
            # return temp
        else:
            # temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            # return temp

    def display(self):
        if (self.front == -1 and self.rear == -1):
            print("Queue is empty")

        else:
            i=self.front
            while i!=self.rear:
                print(self.queue[i])
                i=(i+1)%self.size
            print(self.queue[self.rear])


result=CQueue(5)
result.enqueue(14)
result.enqueue(22)
result.enqueue(13)
result.enqueue(-6)
result.dequeue()
result.dequeue()
result.enqueue(9)
result.enqueue(20)
result.enqueue(5)
result.display()


