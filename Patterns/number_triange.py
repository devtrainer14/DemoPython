for i in range(0,5):
       var = 1
       for j in range(5-i,0,-1):
              print(" ",end = "")
       for k in range(0,i+1):
              print(var,end="")
              var = var+1
       for l in range(0,i):
              var = var-1
              print(var-1,end="")
              
       print("")
