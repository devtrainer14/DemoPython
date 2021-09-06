user = [3,6,4,6]
random = [6,3,4,1]
cow = 0
for i in range(0,len(user)):
	for j in range(i,len(random)):
		if user[i] == random[j]:
			cow=cow+1
			print (cow,i,j)
			break;
		else:
			
			print ("")
			break
for i in user:
	for j in random:
		if i==j:
			
			print ("bull")
			
		else:
			
			print ("NO")
			
			
