#Circular LinkedList
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
        def __int__(self):
            self.head=None

        def insert_begin(self,data):
            temp=self.head
            nb=Node(data)

            while temp.next!=self.head:
                temp=temp.next
            nb.next = self.head
            temp.next=nb
            self.head=nb

        def insert_end(self,data):
            temp = self.head
            ne = Node(data)
            while temp.next!=self.head:
                temp=temp.next

            temp.next=ne
            ne.next=self.head
        def delete_begin(self):
            temp=self.head
            temp2=self.head.next
            while temp.next!=self.head:
                temp=temp.next
            temp.next=temp2
            self.head.next=None
            self.head=temp2

        def delete_end(self):
            prev=self.head
            temp=self.head.next
            while temp.next!=self.head:
                temp=temp.next
                prev=prev.next
            prev.next=self.head
            temp.next=None

        def display(self):

            temp=self.head
            if self.head is None:
                print("Empty")
            else:
                while temp.next!=self.head:
                    print(temp.data)
                    temp=temp.next
                print(temp.data)
#Creation of Linked List
L= Linkedlist()
n1= Node(10)
L.head=n1
n2= Node(20)
n1.next=n2
n3= Node(30)
n2.next=n3
n4= Node(40)
n3.next=n4
n4.next=L.head
L.insert_begin(50)
L.insert_end(60)
L.delete_begin()
L.delete_end()
L.display()