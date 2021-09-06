class parent1:
        def __init__(self,n):
                print("My Parent Default constructor ",n)
                super(parent1,self).__init__()
        def get_print(self):
                print("Parent class 1")


class base1(parent1):
	def __init__(self):
		print("My Base Default constructor")
		super(base1,self).__init__(23)
	def get_print1(self):
		print("base class1")

obj = base1()
obj.get_print()
obj.get_print1()
