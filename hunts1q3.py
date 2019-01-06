n=int(input())
t=0
l=[int(x) for x in input().split()]
for i in range(0,n):
    if(i==l[i]):
        if(t==0):
          print(i,end="")
          t=1
        else:
            print(" ",end="")
            print(i,end="")
if(t==0):
    print("-1")
