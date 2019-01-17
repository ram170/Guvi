a,b=map(str,input().split())
x=[]
y=[]
for i in range(0,len(a)):
    m=a.count(a[i])
    n=b.count(b[i])
    x.append(m)
    y.append(n)
if(x==y):
    print("yes")
else:
    print("no")
