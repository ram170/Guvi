s=input()
d=[]
for i in range(0,len(s)):
    k=ord(s[i])
    if(k>=88):
        k=(k+3)-90+64
    else:
        k=ord(s[i])+3
    d.append(chr(k))
print(''.join(d))    
    
