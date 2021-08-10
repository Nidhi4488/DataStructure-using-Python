#Creation, Traversal, Insertion at the beginning, position, and end
# Deletion at the beginning, position, and end
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
        def __int__(self):
            self.head=None

        def insert_beginning(self,data):
            nb=Node(data)
            nb.next=self.head
            self.head=nb
        def insert_end(self,data):
             ne = Node(data)
             temp = self.head
             while temp.next:
                 temp = temp.next
             temp.next = ne
        def insert_ind(self,data,idx):
            ni=Node(data)
            temp=self.head
            for i in range(idx-1):
                temp=temp.next
            ni.next=temp.next
            temp.next=ni
        def deletion_begin(self):
            temp=self.head
            self.head=temp.next
            temp.next=None
        def deletion_end(self ):
            temp=self.head.next
            temp2=self.head
            while temp.next is not None:
                temp=temp.next
                temp2=temp2.next
            temp2.next=None
        def deletion_pos(self,pos):
            temp=self.head.next
            temp2=self.head
            for i in range (1,pos-1):
                temp=temp.next
                temp2=temp2.next
            temp2.next=temp.next
            temp.next=None


#To traverse Linked List
        def display(self):

            temp=self.head
            if self.head is None:
                print("Empty")
            else:
                while temp:
                    print(temp.data)
                    temp=temp.next

#Creation of Linked List
L= Linkedlist()
n1= Node(10)
L.head=n1
n2= Node(20)
n1.next=n2
n3= Node(30)
n2.next=n3

#insertion at the beginning
# n4= Node(40)
# n4.next=L.head
# L.head=n4
#insertion at the end
# n5=Node(50)
# temp=L.head
# while temp.next:
#     temp=temp.next

# temp.next=n5
#insertion at l index 3
# n=3
# n6=Node(60)
# temp=L.head
# for i in range (n-1):
#     temp=temp.next
# n6.next=temp.next
# temp.next=n6

L.insert_beginning(56)
L.insert_end(34)
L.insert_ind(56,3)
L.deletion_begin()
L.deletion_end()
L.deletion_pos(3)
L.display() #to display linkedlist