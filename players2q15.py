s=list(input())
temp=0
temp2=0
for i in range(0,len(s)):
    n=s.count(s[i])
    if(n>temp):
        temp=n
        temp2=s[i]
print(temp2)        
