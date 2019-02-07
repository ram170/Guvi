n=int(input())
l=[int(x) for x in input().split()]
c=[]
for i in range(0,n):
    x=l.count(l[i])
    c.append(x)
x=c.index(1)
print(l[x])
