str = "i am at btes"
lst3=str.split(" ")
for index in range(len(lst3)-1,-1,-1):
	print(lst3[index].capitalize(),end=" ")

print()
print("===Another Method===")
for data in lst3[::-1]:
       print(data.capitalize(),end=" ")
