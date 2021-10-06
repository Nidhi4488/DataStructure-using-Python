class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.top=None
    def push (self,data):
        nb=Node(data)
        if self.top==None:
            self.top=nb
        else:
            nb.next=self.top
            self.top=nb
    def pop(self):
        if self.top==None:
            print("Empty")
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
    def isEmpty(self):
        if self.top==None:
           print("Empty")
        else:
            print("Not Empty")
    def isFull(self,max_size):
        temp=self.top
        size=0
        if self.top==None:
            print("Empty")
        else:
            while temp:

                temp=temp.next
                size=size+1
        if size>=max_size:
            print("Full")
        else:
            print("Not Full")
    def stackTop(self):
        print(self.top.data)
    def stackBottom(self):
        temp=self.top
        while temp.next!=None:
            temp=temp.next
        print(temp.data)

    def display(self):
        temp=self.top

        if self.top==None:
            print("Empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next


L=LinkedList()
# n1=Node(10)
# L.top=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
L.push(5)
L.push(10)
L.push(20)
# L.pop()
L.isEmpty()
L.display()
L.isFull(3)
L.stackTop()
L.stackBottom()
