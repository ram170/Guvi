n=int(input())
s=list('kabali')
c=0
s.sort()
for i in range(0,n):
    k=list(input())
    k.sort()
    if(k==s):
        c+=1 
print(c)        
