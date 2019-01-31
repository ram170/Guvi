n=int(input())
u=0
l=[int(x) for x in input().split()]
for i in range(0,n-1):
    if(u==1):
        break
    for j in range(i+1,n):
        if(l[i]+l[j]==0):
            u=1
            print(l[i],l[j])
        if(u==1):
            break
            
