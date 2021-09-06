lst = [13,4,5,1,1,10,4]
str=""

if lst[0]>lst[1]:
       for x in range(len(lst)-1):
              if lst[x]>lst[x+1]:
                     str = "Monotonic"
              else:
                     str = "No Monotonic"
                     break
else:
       for x in range(len(lst)-1):
              if lst[x]<lst[x+1]:
                     str = "Monotonic"
              else:
                     str = "No Monotonic"
                     break
print(str)
