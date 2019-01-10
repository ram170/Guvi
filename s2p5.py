n,m=map(int,input().split())
x=[]
for i in range(n+1,m):
    if(i%2==0):
        x.append(i)
for i in range(0,len(x)):
    if(i!=(len(x)-1)):
        print(x[i],end=" ")
    else:
        print(x[i])
     
