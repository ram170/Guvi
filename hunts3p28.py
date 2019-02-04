n=list(input())
s={'\0'}
c=[]
temp=1
for i in range(0,len(n)):
    s.add(n[i])
    if(temp!=len(s)):
        c.append(n[i])
        temp=len(s)
for i in range(0,len(c)):
    if(i!=len(c)-1):
        print(c[i],end="")
    else:
        print(c[i])
        
        
        


