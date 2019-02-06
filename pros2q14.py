def xor(a,b):
    #print(a,b)
    return(a^b)
n,m=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,m):
    x,y=map(int,input().split())
    r=l[x-1]
    for j in range(x,y):
        #print(j)
        r=xor(r,l[j])
    print(r)  
