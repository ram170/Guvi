n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=l.copy()
d=[]
for i in range(0,n):
    c[i]=abs(c[i]-k)
for i in range(0,4):    
 x=min(c)
 y=c.index(x)
 #print(l[y])
 d.append(l[y])
 del c[y]
 del l[y]
del d[0] 
print(*d) 
