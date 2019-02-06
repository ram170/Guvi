def gcd(a,b):
    #print(a,b)
    while(a>0):
        a,b=b%a,a
    return(b)
n,m=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,m):
    x,y=map(int,input().split())
    r=l[x-1]
    for j in range(x-1,y):
        #print(j)
        r=gcd(r,l[j])
    print(r)  
