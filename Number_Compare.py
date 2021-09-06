a= int(input("Enter a = "))
b= int(input("Enter b = "))
c= int(input("Enter c = "))

if(a>b):
	if(a>c):
		print("a is greaterest ",a)
	else:
		print("c is greaterest ",c)
else:
	if(b>c):
		print("b is greaterest ",b)
	else:
		print("c is greaterest ",c)