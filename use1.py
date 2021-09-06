pins = [(1234,1000,[+100,-200]),
(1235,5000,[-100,+200]),
(1236,7000,[+350,+500]),
(1237,500,[-250,+450])]
count = 0
balance = 100000
x = len(pins)
transact = []
status = 0
	
##################################### Matching Pin ##########################################

def match(pin):
	global count
	global status
	global balance
	for i in pins:
		# if(x < 4):
	# for j in i:
		if(count < 4):
			if(pin == i[0]):
				#b = 1
				print(i)
				status = 1
				balance = i[1]
				for k in i[2]:
					transact.append(k)
				# print(transact)
				# print(balance)
				break
				count = count + 1			
			elif(pin != i[0]):
				status = 0
				#b = 0
				# print(count)
					# break
		elif(count > 3):
			exit()
	count =count +1
		# elif( x > 4):
			# exit()			
	if(status == 1):
		print("MATCH FOUND")
		menu(pin)
	elif(status == 0):
		if(count < 3):
			wrongpin()
		if(count >= 3):
			block()
			exit()
	return status

#################################### Block Account ##########################################
def block():
	print("Your account is BLOCKED. Please contact bank...... ")


#################################### Wrong Pin ##############################################
def wrongpin():
	pin = int(input("Wrong Pin. Please try again... "))
	match(pin)

#################################### Options Menu ###########################################	
def menu(pin):
	print("1. Press 1 for Withdrawl")
	print("2. Press 2 to Deposit")
	print("3. Press 3 for Balance Enquiry")
	print("4. Press 4 for Mini Statement")
	print("5. Exit")
	option = int(input("Enter the number from above options: "))
	if(option == 1):
		withdrawl()
	elif(option == 2):
		deposit()
	elif(option == 3):
		enquiry()
	elif(option == 4):
		statement()
	elif(option == 5):
		exit()

################################### Cash Withdrawl #########################################
def withdrawl():
	global balance
	global transact
	amount = int(input("Enter the amount to be withdrawn: "))
	if(balance > 0 and balance>amount):
		balance = balance - amount
		print("###########################################################")
		print("***********************************************************")
		print("                   Amount Deducted... ", amount)
		print("***********************************************************")
		print("###########################################################")
		next = input("Do you want to withdraw more. Press y for yes and n for no: ")
		if(next == "y"):
			withdrawl()
		elif(next == "n"):
			print("###########################################################")
			print("***********************************************************")
			print("    THANK YOU!!! Now Your current balance is: ", balance)
			print("***********************************************************")
			print("###########################################################")
			transact.append(amount * -1)
			menu(pin)
	# elif(balance < amount):
	# 	print("Balance is lower than Entered Amount... ")
	else:
		print("Balance not Sufficient... ")

#################################### Cash Deposit ##########################################
def deposit():
	global balance
	global transact
	amount = int(input("Enter the amount to be deposited: "))
	if(amount > 0):
		balance = balance + amount
		print("###########################################################")
		print("***********************************************************")
		print("                 Amount Deposited... ")
		print("***********************************************************")
		print("###########################################################")
		print("Now Your current balance is: ", balance)
		transact.append(amount)
		menu(pin)
	else:
		print("Please enter a valid amount....... ")

################################### Balance Enquiry ########################################
def enquiry():
	global balance
	print("###########################################################")
	print("***********************************************************")
	print("           Your current Balance is: ", balance)
	print("***********************************************************")
	print("###########################################################")
	menu(pin)

################################### Balance Enquiry ########################################
# def check(z):
# 	x = 0
# 	if(z > 0):
# 		x = 1
# 	elif(z < 0):
# 		x = 0
# 	return x

################################### Mini Statement #########################################
def statement():
	# print("Statement")
	global transact
	#ssglobal stats
	print()
	print("                        Mini Statement for ", pin, " is:                         ")
	print("------------------------------------------------------------------------------")
	m = len(transact)
	for j in transact:
		if(j > 0):
		 	print("                   ",j,"  	    		was deposited")
		if(j < 0):
	 		print("                   ",j*-1, "     			was withdrawn")






key = input("Welcome User..! Press 'y' to Continue, Other Key to Exit.")
if(key != "y"):
	exit()	
else:
	pin = int(input("Enter a pin: "))
	match(pin)	