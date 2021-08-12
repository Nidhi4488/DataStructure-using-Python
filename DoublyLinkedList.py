class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head.prev=nb
        self.head=nb

    def insert_end(self,data):
        ne= Node(data)
        temp= self.head
        while temp.next:
            temp=temp.next
        ne.prev=temp
        temp.next=ne

    def insert_pos(self,data,n):
        np=Node(data)
        temp=self.head
        temp2=self.head.next
        for i in range (1,n-1):
            temp2=temp2.next
            temp=temp.next

        np.next=temp.next
        temp.next=np
        np.prev=temp
        temp2.prev=np

    def delete_begin(self):
        temp=self.head
        self.head.next.prev=None
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        before=self.head
        temp=self.head.next
        while temp.next!=None:
            before=before.next
            temp=temp.next
        before.next=None
        temp.prev=None

    def delete_pos(self,n):
        temp=self.head.next
        before=self.head
        for i in range (1,n-1):
            temp=temp.next
            before=before.next
        temp.next.prev=temp.prev
        before.next=temp.next
        temp.next=None
        temp.prev=None






DL=DoublyLL()
n1=Node(10)
DL.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
DL.insert_begin(40)
DL.insert_end(50)
DL.insert_pos(60,2)
DL.delete_begin()
DL.delete_end()
DL.delete_pos(2)
DL.display()
