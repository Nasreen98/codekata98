print("stack implementation")
stack=[]
while True:
    print("which stack you want?\n 1.,2.pop,3.size,4.emptiness,5.exit")
    a=int(input())
    if a==1:
        print("enter the element you want to insert:"
        l=input()
        stack.append(l)   
        print("Elements in stack are:",stack)
    elif a==2:
        if stack==[]:
            print("empty stack you cannot delete!!")
        else:   
            stack.pop()
            print("elements in stack are:",stack)
    elif a==3:
        print("size of stack is:",len(stack)
           
    elif a==4:
         if stack==[]:
             print("your stck is empty!!")
         else:
             print("you have",len(stack),"elements is not stack")
                 
    elif a==5:
         print("exit")
         break      

    
   
