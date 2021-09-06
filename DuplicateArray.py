a1 = [(4,6),(4,6),(7,9),(5,1),(7,9),(5,1),(4,6)]
#a1=[('a', 'e'), ('b', 'x'), ('b', 'x'),('a', 'e'), ('b', 'x')]
x= len(a1)
for i in range(0,x):
	for j in range(0,len(a1[i])):
		print(a1[i][j],end=" ")
	print()










"""for j in range(0,x):
	for k in range(j+1,x):
		if(a1[j][0] == a1[k][0]):
			if(a1[j][1]==a1[k][1]):
				print(a1[j])
"""