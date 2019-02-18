x=int(raw_input())
y=0
for i in range(2,x//3):
    if (x%i==0):
        y=y+1
    if(y<=0):
        print('yes')
    else:
        print('no')
