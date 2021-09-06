"""r = lambda q: q * 2
s = lambda q: q * 3
x = 2
x = r(x) 
x = s(x) 
x = r(x) 
print x 

-------------------------------------------------------------------------------------------------------------------

a = 4.5
b = 2
print a//b 
-----------------------------------------------------------------------------------------------------------------------
"""
a = True
b = False
c = False
if a or b and c: 
    print("GEEKSFORGEEKS")
else: 
    print("geeksforgeeks")
------------------------------------------------------------------------------
a = True
b = False
c = False
  
if not a or b: 
    print 1
elif not a or not b and c: 
    print 2
elif not a or b or not b and a: 
    print 3
else: 
    print 4

----------------------------------------------------------------
count = 1 
  
def doThis(): 
  
    global count 
  
    for i in (1, 2, 3):  
        count += 1
  
doThis() 
  
print count 
"""