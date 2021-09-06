l=['a','c','b','f','e','z','s']
l1=[]
while l:
	min=l[0]
	for i in l:
        # here **ord** means we get the ascii value of particular character.
		if ord(min)>ord(i):
			min=i
		l1.append(min)
		l.remove(min)
print(l1)