n=int(input())
s=list(input())
c=[]
for i in range(0,n):
    if(s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' and s[i]!='A' and s[i]!='E' and s[i]!='O' and s[i]!='U' and s[i]!='I'):
        c.append(s[i])
c.reverse()
print(''.join(c))
    
