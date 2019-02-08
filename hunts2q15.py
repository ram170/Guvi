n=int(input())
l=[int(x) for x in input().split()]
x=[]
y=[]
for i in range(0,n):
    d=c=u=0
    for j in range(0,n):
      if(i==0):
        #print(x)
        if(l[i]>l[j] and i!=j):
                c+=1
               # print(c)
        if(j==n-1 and j==c):
            y.append(l[i])
            x.append(l[i])
        #print(j,c)    
      elif(i==n-1):
        if(i!=j):
            d+=1
            if(l[i]>l[j]):
                c+=1
        if(j==n-1 and d==c):
            y.append(l[i])
        if(j==n-1):
            x.append(l[i])
        #print(d,c)    
      else:        
        if(j<i):
            #print(l[i],l[j])
            if(l[i]>l[j]):
                u+=1 
            #print(i,u)    
        elif(j>i):
            d+=1
            if(l[i]>l[j]):
                c+=1
        if(j==n-1 and d==c):
            x.append(l[i])
        if(j==n-1 and d==c and i==u ):
            y.append(l[i])
print(*x)
print(*y)
            
