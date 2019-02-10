n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
    x,y=map(int,input().split())
    temp=999999999
    for j in range(x-1,y):
        if(l[j]<temp):
            temp=l[j]
    print(temp)        
        
