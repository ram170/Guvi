n=int(input())
u=0
a=[]
b=100000000
l=[int(x) for x in input().split()]
for i in range(0,n-1):
  if(u==1):
        break
  for j in range(i+1,n):
      a=l[i]+l[j]
      if(a==0):
          u=1
          print(l[i],l[j])
          break;
      elif(abs(a)<abs(b)):
          b=a
          c=l[i]
          d=l[j]
if(u!=1):
    print(c,d)
          
          
        
            
