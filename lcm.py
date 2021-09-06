x=6
y=10
if x>y:
	small = y
	big=x
else:
	small=x
	big=y
lcm = 1
for i in range(big,1,-1):

	if((big%i==0) and (small%i==0)):
		lcm=lcm*i
		small = small/i
		big=big/i
lcm=lcm*big*small
print(lcm)
hcf = (x*y)/lcm
print(hcf)
