import sqlite3
db = sqlite3.connect("MyDataBase")
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
Create Table
 
cur.execute("Create table if not exist tb_Emp(id INTEGER 
PRIMARY KEY, name TEXT, pass Text)")
db.commit()

cur.execute("Create table if not exist tb_Salary(Sal_id INTEGER 
PRIMARY KEY, Salary TEXT, Designation Text, E_id Integer Not Null,  FOREIGN KEY (E_id) REFERENCES tb_Emp(id))")
db.commit()
# Insert Query

"""i = cur.execute("Insert into tb_First(id, name) 
	VALUES(?,?)",(3,"Rupinder"))
db.commit()
if i:
 print("Successfull")
else:
 print("Try Again") 
 """
cur.execute("Select * from tb_First ")
for i in cur:
	print(i[0])
	print ('{0}, {1}'.format(i[0],i[1]))
	
db.commit()