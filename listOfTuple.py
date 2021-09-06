list = [(3,9),(4,7),(2,7),(3,9),(4,7)]


count = 0
for i in list:
	for j in i:
		print("Tuple :: ",i ," = ",j)
	#print(i)
list1=[]
tup = list[0]
list2 = []
for i in range(0,len(list)):
	for j in range(0,len(list[i])):
		if list[i] in list1:
			count = count+1
			list2.append(list[i])
		else:
			list1.append(list[i])
			print (list1)
			break

print (list2)