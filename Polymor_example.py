class dog(object):
       def sound(self):
              print("Woof Woof")

class bear(object):
       def sound(self):
              print("Groarr")

def makesound(obj):
       obj.sound()

obj1 = dog()
obj2 = bear()

x = int(input("Press 1 for dog \nPress 2 for bear \nEnter Your Choice :: "))

if(x==1):
       makesound(obj1)
else:
       makesound(obj2)


