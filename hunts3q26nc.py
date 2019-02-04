n=int(input())
l=[int(x) for x in input().split()]
l.reverse()
for i in range(0,n):
    if(i!=n-1):
        print(l[i],end="->")
    else:
        print(l[i],end="")
        
