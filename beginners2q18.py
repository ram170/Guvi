n,m=map(int,input().split())
for i in range(n,m):
 x=i
 u=0
 t=0
 while(x>0):
    c=x%10
    c=c*c*c
    t=t+c
    x=int(x/10)
    #print(t)
 if(t==i):
   if(u==1):  
    print(" ")
    print(t,end="")
   else:
       print(t,end=" ")
       u=1
    
 
    
