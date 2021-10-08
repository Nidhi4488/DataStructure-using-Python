#!/bin/python3

def rotateLeft(d, arr):
    # Write your code here
    n= len(arr)
    for j in range (d):
        temp= arr[n-1]
        arr[n-1]= arr[0]
        for i in range (0,n-2):
            arr[i]=arr[i+1]
        arr[n-2]=temp
    print(arr)
def secondMethod(d,arr):
    for i in range (d):
        arr.append(arr.pop(0))
    print(arr)


rot=1
a=[4,7,2,8,1,5,9]
rotateLeft(rot,a)
secondMethod(rot, a)
