n,s=map(int,input().split())
v=[]
l=[int(x) for x in input().split()]
for i in range(0,n-1):
    k=[int(x) for x in input().split()]
    for j in range(0,s):
        l.append(k[j])
for i in range(0,s):
    d=l.count(l[i])
    if(d>=n):
        v.append(l[i])
for i in range(0,len(v)):
    if(i!=len(v)-1):
        print(v[i],end=" ")
    else:
        print(v[i])
