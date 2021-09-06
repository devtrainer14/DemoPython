a = [1, 1, 2, 3, 5, 5, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10, 11, 12, 13,13]
limit=[]
for x in a:
      if(x in b and x not in limit):
              limit.append(x)
                     
print(limit)
       
