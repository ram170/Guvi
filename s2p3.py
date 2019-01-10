n=list(input())
x=[]
for i in range(0,len(n)):
    x.append(n[i])
#print(n)
x.reverse()
#print(n,x)
if(n==x):
    print("yes")
else:
    print("no")
    
