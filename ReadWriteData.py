obj=open("abcd.txt","w")  
obj.write("Hi, How are You..!! Welcome to the world of Python")  
obj.close() 
obj1=open("abcd.txt","r")  
s=obj1.read()  
print (s)  
obj1.close() """ 
obj2=open("abcd.txt","r")  
s1=obj2.read(20)  
print (s1)  
obj2.close()"""