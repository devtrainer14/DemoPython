def pattern(n): 
  
    # for loop for rows 
    for i in range(1,n+1): 
  
        # conditional operator 
        if(i % 2 != 0):
            k =i + 1 
        else:
            i 
  
        # for loop for printing spaces 
        for g in range(k,n): 
            if g>=k: 
                print(end="  ") 
  
        # according to value of k carry 
        # out further operation 
        for j in range(0,k): 
            if j == k - 1: 
                print(" * ") 
            else: 
                print(" * ", end = " ") 
  
  
# Driver code 
n = 10
pattern(n)
#===========================================================


dict = {}
i=0
while i<3:
       i = i+1
       name = input("Enter name")
       dob = input("Enter dob")
       dict[name]=dob
print(dict)
name_key = input("Enter name to find the birthday:")
print("Hi ",name_key," Your Bith Date is ",dict[name_key])
