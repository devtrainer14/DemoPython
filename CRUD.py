import sqlite3
db = sqlite3.connect("BTES")  # Not providing hostname or anything becz sqlite3 doesn't run on separate dp
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
#Create Table
#cur.execute("Create table tb_cuts(id INTEGER PRIMARY KEY, name TEXT)")
#db.commit()
# Insert Query
"""
i = cur.execute("Insert into tb_cuts(id, name) VALUES(?,?)",(2,"Sipika Saini"))
db.commit()
if i:
 print("Successfull")
else:
 print("Try Again")  

#Fetch Data from Table
cur.execute("Select * from tb_cuts")
print(cur.fetchall()) 
"""
#Fetch Data from Table using clause
cur.execute("Select * from tb_cuts where id = ?",(2,))
#print(cur.fetchall()) 

for i in cur:
	print(i[0])
	print ('{0}, {1}'.format(i[0],i[1]))
"""
# Update the table
x=cur.execute("update tb_cuts set name = ? where id = ?",("Sipika Summan",1))
db.commit()
if x:
 print ("updated")
else:
 print ("Not Done")"""

# Delete the table

x=cur.execute("delete from tb_cuts where id = ?",(2,))
db.commit()
if x:
 print ("Deleted")
else:
 print ("Not Done")

