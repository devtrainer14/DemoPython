#a1 = [(4,6),(7,9),(5,1),(4,6)]
a1 = [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x')] 
x= len(a1)

count=0
for j in range(0,x):
	for k in range(j+1,x):
		if(a1[j] == a1[k]):
			if(a1[j][1]==a1[k][1]):
				del a1[k]
				x=x-1
				count=count+1
print(a1)
print(count)