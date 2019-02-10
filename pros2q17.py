n,k=map(int,input().split())
f=0
l=[int(x) for x in input().split()]
for i in range(0,n):
    for j in range(0,n):
        if(i!=j):
            if(l[i]+l[j]==k):
                f=1
                break
if(f==0):
    print("no")
else:
    print("yes")
