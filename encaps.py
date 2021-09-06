class Sample_encap:
       __a=90 #private
       b=9     #public
       def __init__(self):
             self._c=50 
       
       def modify(s):
              s.__a=100
              s.b=23
       def show(s):
              print(s.__a)
              print(s.b)
              print(s._c)
              

class Child_encap(Sample_encap):
       def show1(s):
              #print(s.__a)
              print(Sample_encap.b)
              print(s._c) 

obj = Child_encap()
#obj.modify()
#obj.show()
#obj.show()
