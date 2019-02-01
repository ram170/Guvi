n=int(input())
for i in range(0,n):
	for j in range(0,n):
		k=int(input())
		l[i][j].append(k)
for i in range(0,n):
	for j in range(0,n):
	  if(l[i][j]==1):	
		if(i==0 and j==0):
				if(l[i+1][j]+l[i][J+1]==0):
					c+=1
				#if(l[i])	
		elif(i==n-1 and j==0):
			if(l[i-1][j]+l[i][j+1]==0):
				c+=1
		elif(i==0 and j==n-1):
			if(l[i][j-1]+l[i+1][j]==0):
				c+=1
		elif(i==n-1 and j==n-1):
			if(l[i][j-1]+l[i-1][j]==0):
				C+=1
		elif(i==0 and j!=0):
			if(l[i][j+1]+l[i][j-1]+l[i+1][j]==0):
				c+=1
		elif(j==0 and i!=0):
			if()
			
