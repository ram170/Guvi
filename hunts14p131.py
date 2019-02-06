n=int(input())
l=[int(x) for x in input().split()]
l.sort()
l.reverse()
c=[]
if(i%2==0):
    f=0
    b=n-1
    for i in range(0,n/2):
      if(f+i!=b-i):    
        c.append(l[f+i])
        c.append(l[b-i])
else:
    f=0
    b=n-1
    for i in range(0,int(n/2)+1):
        if(f+i<b-i):
            c.append(l[f+i])
            c.append(l[b-i])
        else:
            c.append(l[f+i])
print(*c)            
            
