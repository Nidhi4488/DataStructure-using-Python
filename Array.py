import array as arr

#List is implemented as dynamic array
Stock_price= [280, 456, 345, 213,654]
#to get values by index order is O(1)
print(Stock_price[4])
print(Stock_price[2])

#to get the index order is O(n) in worst case where is size of array
for i in range (0,len(Stock_price)):
    if Stock_price[i] == 456:
        print("The index is:" + str(i))

#Array Traversal order is O(n)
print("The values of Stock Price:")
for i in Stock_price:
    print(i)

#Array insertion order is O(n)
print("The new array after insertion:")
Stock_price.insert(2,421)
for i in Stock_price:
    print(i)

#Array deletion order is O(n)
print("The new array after deletion:")
Stock_price.remove(345)
for i in Stock_price:
    print(i)

#Taking array input from user
a=[]
n= int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    a.append(ele)
print("The array created is:")
for i in a:
    print(i)
print()

#min and max function
print("The maximum number in array a:" + str( max(a)))
print("The minimum number in array a:"+ str( min(a)))

#Array of Strings
array= ["apple", "Ball", "Cat"]
#2D array
arr1=[[2,3,4],[5,6,7]]
for i in arr1:
    print(i)

print(arr1[0][1])

#we can also create array this way
newarray= arr.array('i', [1,4,2,5,6])
for i in range(0, len(newarray)):
    print(newarray[i])
print("Another way of traversal:")
for i in newarray:
    print(i)