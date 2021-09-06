class MyError(Exception):
       def _init_(self,data):
              print(data)


try:
       raise MyError("Please Handle It")
except MyError as e:
       print("Handled",e)
