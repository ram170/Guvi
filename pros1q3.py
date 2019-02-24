a,b=map(str,input().split())
u=0
for i in range(0,len(a)):
    if(a[i]==b[i]):
        u+=1
print(len(b)-u)        
