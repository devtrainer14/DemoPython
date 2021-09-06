listt = [6,4,5,3,2,3,4]
try:  
    a=listt[10]/0  
    print (a)  
except ArithmeticError:  
        print ("This statement is raising an exception" ) 
except Exception as e:
	print("Exception 2......",e)
finally:
	print("Finally Excecution")

print("Rest Code")
