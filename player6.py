m,n=input().split()
u=0
for i in range(0,len(m)):
    if(m[i]!=n[i]):
        u+=1
    if(u>1):
        break;
if(u<=1):
    print("yes")
else:
    print("no")
