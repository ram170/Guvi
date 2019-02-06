k=int(input())
l=[]
q=[]
for i in range(0,k):
    l=[int(x) for x in input().split()]
    for j in range(0,len(l)):
        q.append(l[j])
    l=[]    
q.sort()
print(*q)
