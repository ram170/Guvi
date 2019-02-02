n=int(input())
l=[int(x) for x in input().split()]
u=1
t=0
l.sort()
for i in range(0,n):
    if(i==0):
        t=t+u
    elif(l[i]==l[i-1]):
        t=t+u
    else:
        u+=1
        t=t+u
print(t,end="")        
        
    
