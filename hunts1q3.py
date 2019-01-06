n=int(input())
t=0
l=[int(x) for x in input().split()]
for i in range(0,n):
    if(i==l[i]):
        t=1
        print(i,end=" ")
if(t==0):
    print("-1")
