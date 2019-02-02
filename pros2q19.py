k=int(input())
l=[]
q=[]
for i in range(0,k):
    l=[int(x) for x in input().split()]
    for j in range(0,len(l)):
        q.append(l[j])
    l=[]    
q.sort()
for i in range(0,len(q)):
    if(i==0):
        print(q[i],end="")
    else:
        print(" ",q[i],end="")
