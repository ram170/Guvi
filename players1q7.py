n=input()
l=[]
for i in range(0,len(n)-1,2):
    l.append(n[i+1])
    l.append(n[i])
print("".join(l))    
    
    
