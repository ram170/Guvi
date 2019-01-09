n=int(input())
s=0
while(n>0):
    x=n%10
    s=s+(x*x)
    n=int(n/10)
print(s)    
