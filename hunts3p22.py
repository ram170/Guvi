def prod(l):
    k=1
    for i in range(0,len(l)):
        k=k*l[i]
    return k    
n=int(input())
l=[int(x) for x in input().split()]
c=prod(l)
d=[]
for i in range(0,n):
    k=int(c/l[i])
    d.append(k)
print(*d)    

    
