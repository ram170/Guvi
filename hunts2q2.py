n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l.sort()
l.reverse()
print(l[k-1])
