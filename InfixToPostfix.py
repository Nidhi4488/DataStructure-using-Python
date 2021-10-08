# class infix_to_postfix:
#     precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
#     def __init__(self):
#         self.items=[]
#         self.size=-1
#     def push(self,value):
#         self.items.append(value)
#         self.size+=1
#     def pop(self):
#         if self.isEmpty():
#             return 0
#         else:
#             self.size-=1
#             self.items.pop()
#     def isEmpty(self):
#         if (self.size==-1):
#             return True
#         else:
#             return False
#     def peek(self):
#         if self.isEmpty():
#             return False
#         else:
#             return self.items[self.size]
#     def isOperand(self,i):
#         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             return True
#         else:
#             return False
#     #Main function
#     def infixtopostfix(self,exp):
#         postfix=""
#         print('postfix expression after every iteration is:')
#         for i in exp:
#             if (len(exp)%2==0):
#                 print("Incorrect exression")
#                 return False
#             elif(self.isOperand(i)):
#                 postfix +=i
#             elif(i in '^+*-/'):
#                 while(len(self.items)and self.precedence[i]<=self.precedence[self.peek()]):
#                     postfix+=self.pop()
#                 self.push(i)
#             elif i is '(':
#                 self.push(i)
#             elif i is ')':
#                 o=self.pop()
#                 while o!='(':
#                     postfix +=o
#                     o=self.pop()
#             print(postfix)
#         while len(self.items):
#             if (self.seek()=='('):
#                 self.pop()
#             else:
#                 postfix+=self.pop()
#             return postfix
#
#
#
#
# s=infix_to_postfix()
# exp=input('Enter the expression:')
# result=s.infixtopostfix(exp)
# if (result!=False):
#     print("The postfix is:",result)
#
class infix_to_postfix:
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    def __init__(self):
        self.items=[]
        self.size=-1
    def push(self,value):
        self.items.append(value)
        self.size+=1
    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def isempty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def seek(self):
        if self.isempty():
            return false
        else:
            return self.items[self.size]
    def isOperand(self,i):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        else:
            return False
    def infixtopostfix (self,expr):
        postfix=""
        print('postfix expression after every iteration is:')
        for i in expr:
            if(len(expr)%2==0):
                print("Incorrect infix expr")
                return False
            elif(self.isOperand(i)):
                postfix +=i
            elif(i in '+-*/^'):
                while(len(self.items)and self.precedence[i]<=self.precedence[self.seek()]):
                    postfix+=self.pop()
                self.push(i)
            elif i is '(':
                self.push(i)
            elif i is ')':
                o=self.pop()
                while o!='(':
                    postfix +=o
                    o=self.pop()
            print(postfix)
                #end of for
        while len(self.items):
            if(self.seek()=='('):
                self.pop()
            else:
                postfix+=self.pop()
        return postfix
s=infix_to_postfix()
expr=input('Enter the expression: ')
result=s.infixtopostfix(expr)
if (result!=False):
    print("the postfix expression is:",result)