k=list(input())
s=k.copy()
u=0
if(len(s)%2==0):
    for i in range(0,int(len(s)/2)):
        if(s.pop()==s[i]):
            u+=1 
    #print(len(k))        
    if((u*2)==len(k)):
      print("YES")
    else:
      print("NO")        
else:
    for i in range(0,int(len(s)/2)):
        if(s.pop()==s[i]):
            u+=1 
        #print(u)    
    if((u*2)+1==len(k)):
      print("YES")
    else:
      print("NO")
            
