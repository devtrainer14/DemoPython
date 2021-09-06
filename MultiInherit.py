class Multi_Parent1:
	def __init__(self,y):
		super(Multi_Parent1,self).__init__()
		print("Parent 1",y)


class Multi_Parent2:
	def __init__(self,x):
		super(Multi_Parent2,self).__init__()
		print("parent 2",x)

class Multi_base(Multi_Parent2,Multi_Parent1):
	def __init__(self,n):
		print("Base Class")
		super().__init__(self,3)

Multi_base(6)
