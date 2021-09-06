# cyclic rotation
#array a of n integers
#k tells rotation number
#A,K,N
#Solution(int[] A, int K)

A=[]
y = int(input("Enter no of elements of array between 1 and 100"))
if y > 100 or y <1:
	print("Enter valid range")
	y = int(input("Enter no of elements of array between 1 and 100"))
	
#x= int(input("Enter integer between -1000 and 1000 to append to list"))

for i in range(0,y):
	x = int(input("Enter element"))
	if x <-1000 or x >1000:
		print("Number should be between -1000 and 1000")
		i=i-1
		break
	A.append(x)

#print(A)
def rotate(a,k):
	for i in range(1,k+1):
		for i in range(0,len(a)-1):
			temp=a[i+1]
			a[i+1]=a[0]
			a[0]=temp
	return a
	
B=True
while B:
	k = int(input("Enter rotation value between 1 to 100"))
	if k>100 or k<1:
		print("Enter correct range")
	else:
		B=False
		
m=rotate(A,k)
print(m)

#a=[2,3,4]
#k=1
#for i in range(0,len(a)-1):
	#temp=a[i+1]
	#a[i+1]=a[0]
	#a[0]=temp
#print(a)
	
	

	
	