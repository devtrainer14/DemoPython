list1=[]
num = int(input("Enter the number of elements in list:- "))
for i in range(0,num):
	element=int(input("Enter the number:- "))
	list1.append(element)
print(list1)
number_of_loop = int(input("Enter the number of rotations:- "))
for i in range(0,number_of_loop):
	# list2=[]
	# abc =list1[num]
	for j in range(num-1,0,-1):
		a = list1[j-1]
		list1[j-1]=list1[j]
		list1[j] = a
	print(list1) 
