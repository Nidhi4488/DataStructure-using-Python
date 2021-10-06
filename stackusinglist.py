from collections import deque
from queue import LifoQueue

# stack using list
list1=[1,2,4,5,6]
print(list1.pop()) #to pop
print(list1)
list1.append(7) #to push
# to get last element without poping i.e. top element
print(list1[-1])


#the problem with list is it is dyanamic array, everytime capacity gets over new capacity is allocated by allocating new memory space with more capacity hence all the elements need to be copied again
#hence using list as stack in python is not recommended
#deque is recommended
stack= deque()
print(dir(stack)) #to check the methods of deque
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

#3rd method
print("Using queue class for implementing stack" )
stack3=LifoQueue(maxsize=3)
print(stack3.qsize())
stack3.put(1)
stack3.put(2)
stack3.put(3)
print("Stack full:",stack3.full())
print("Stack size:",stack3.qsize())
#to pop
stack3.get()
stack3.get()
stack3.get()
print("Stack Empty:", stack3.empty())


