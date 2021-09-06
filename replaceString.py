#cursing @ btes
obj = open("curse.txt","r")
s=obj.read()
obj.close()
k =["stupid","bitch","foolish","moron"]
for i in range(0,len(k)):
	if k[i] in s:
		m=""
		for  z in range(0,len(k[i])):
			m=m+"*"
		s=s.replace(k[i],m)
obj2 = open("curse.txt","w")
obj2.write(s)
obj2.close()
