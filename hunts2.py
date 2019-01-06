n=int(input())
l=[int(x) for x in input().split()]
l.sort()
l.reverse()
s=str(l[0])
if(l.count(0)==n):
    print('0')
else:    
  for i in range(1,n):
    s=s+str(l[i])
  print(s)    
