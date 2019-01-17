n=list(input().split())
b=[]
for i in range(0,len(n)):
    b=list(n[i])
    b.reverse()
    if(i!=len(n)-1):
      print(''.join(b),end=" ")
    else:
        print(''.join(b),end="")
