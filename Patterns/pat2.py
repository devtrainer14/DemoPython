for i in range(1,6):
	for j in range(4-i+1):
		print(end="  ")
	if(i%2!=0):	
		print(i*"  * ",end=" ")
	
	print()