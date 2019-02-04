n,m=map(int,input().split())
u=0
l=[int(x) for x in input().split()]
for i in range(0,n-1):
    for j in range(i+1,n):
        if(l[i]+l[j]==m):
            u=1
            break;
if(u==0):
    print("NO")
else:
    print("YES")
