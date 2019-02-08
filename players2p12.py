n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
    x=l[n-1]
    l=[x]+l
    del l[n]
print(*l)    

    
