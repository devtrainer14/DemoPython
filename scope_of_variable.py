a = 100;
def hello():
	x=20
	global a
	a=a+20
	x=x+1
	print(a)
	print(x)
#print(x)
print(a)
hello()