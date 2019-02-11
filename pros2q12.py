n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
    x,y=map(int,input().split())
    c=0
    for j in range(x-1,y):
        c=c+l[j]
    print(c)    
        
