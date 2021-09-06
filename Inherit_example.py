from Myclass import Myclasss
from encaps import Sample_encap
from Patterns.pat1 import patt1

class My_Class1(Myclasss):
       def MyMethod(self,h):
              print("Method1 from class1 :: ",h)

class My_Class2(My_Class1):
       def MyMethod1(self):
              print("Method2 from class2")

obj = My_Class2()
obj.MyMethod(34)
obj.MyMethod1()
obj.func(34)
obj1 = Sample_encap()
obj1.modify()
obj1.show()
print(obj1._c)
o = patt1()
o.method1()
