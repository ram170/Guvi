n=int(input())
l=[int(x) for x in input().split()]
l.sort()
for i in range(0,n,2):
    if(i==n-1):
        print(l[n-1])
    else:    
     if(l[i]!=l[i+1]):
        print(l[i])
        break;
