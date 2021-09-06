import Sample_encap
class Myclasss:
	"This is my class"
	a = "value"
	def func(s,n):
		print ("Value2 :: ",n)
		return n

print(Sample_encap._c)


#In Python, this:

#my_object.method("foo")
#... is syntactic sugar, which the interpreter translates behind the scenes into:

#MyClass.method(my_object, "foo")
#... which, as you can see, does indeed have two arguments - it's just that the first one is implicit, from the point of view of the caller.

#This is because most methods do some work with the object they're called on, so there needs to be some way for that object to be referred to inside the method. By convention, this first argument is called self inside the method definition:


