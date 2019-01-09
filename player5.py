s=list(input().split())
y=[]
v=0
#print(s)
for i in range(0,len(s)):
    x=s[i]
    #print(x[0])
    if(x[0].islower()):
        v=32
    #print(ord(x[0]))
    l=ord(x[0])-v
    c=chr(l)
    x=x[:1].replace(x[0],c)+x[1:]
    v=0
    print(x,end=" ")
