#Maximum element
def getMax(operations):
    # Write your code here
    stack = []
    maximum = []
    for q in operations: #operations = ['1 97', '2', '1 20', ....]
        q = list(map(int, q.split()))

        if q[0] == 1:
            if stack:
                stack.append(max(stack[-1], q[1]))
            else:
                stack.append(q[1])
        elif q[0] == 2:
            stack.pop()
        else:
            maximum.append(stack[-1])
    return maximum

#Balanced Brackets
stack = []
parenthesis = {'(': ')', '{': '}', '[': ']'}

for i in s:
    if i in ['(', '{', '[']:
        stack.append(i)
    else:
        if stack:
            top = stack.pop()
            if parenthesis[top] != i:
                return 'NO'

        else:
            return 'NO'
return 'NO' if stack else 'YES'

#Equal Stacks
def equalStacks(h1, h2, h3):
    # Write your code here
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    while h1 and h2 and h3:
        mini=min(s1,s2,s3)
        while s1>mini:
            s1=s1-h1.pop(0)
        while s2>mini:
                s2=s2-h2.pop(0)
        while s3>mini:
            s3=s3-h1.pop(0)
        if (s1==s2==s3):
            return s1
    return 0

#Game of two stacks
def twoStacks(maxSum, a, b):

    i = j = maxnum = total = 0
    while (i < len(a) and total + a[i] <= maxSum):
        total += a[i]
        i += 1
        maxnum += 1
    while (j < len(b) and i > 0):
        total += b[j]
        j += 1
        while (i > 0 and total > maxSum):
            i -= 1
            total -= a[i]

        if total <= maxSum and maxnum < i + j:
            maxnum = i + j
    return maxnum


#Largest Rectangle
def largestRectangle(h):
    # Write your code here
    stack=[]
    area=i=0
    h.append(0)
    while i < len(h):
        if not stack or h[stack[-1]]<h[i]:
            stack.append(i)
            i+=1
        else:
            top=stack.pop()
            area=max(area, h[top]*(i-stack[-1]-1 if stack else i))
    return area


#Waiters
def waiter(number, q):
    # Write your code here
    primenum = []
    i = 2
    p = 0
    answers = []

    A = []
    B = []

    def isprime(i):
        for k in range(2, int(i / 2) + 1):
            if i % k == 0:
                return False
        return True

    while p < q:
        if isprime(i):
            primenum.append(i)
            p += 1
        i = i + 1

    for i in range(q):
        while (number):

            top = number.pop()
            if (top % primenum[i] == 0):
                B.append(top)
            else:

                A.append(top)

        while (B):
            answers.append(B.pop())

        number = A
        A = []
    while (number):
        answers.append(number.pop())

    return answers


#AND xor OR

def andXorOr(a):
    # Write your code here
    stack=[]
    maxresult=0
    for i in a:
        while stack:
            result=stack[-1]^i
            maxresult=max(maxresult, result)
            if stack[-1]>i:
                stack.pop()
            else:
                break
        stack.append(i)
    return maxresult