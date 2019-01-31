n=int(input())
x=n
t=0
while(x>0):
    c=x%10
    c=c*c*c
    t=t+c
    x=int(x/10)
    #print(t)
if(t==n):
    print("yes")
else:
    print("no")
    
