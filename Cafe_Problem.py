# mycursor = mydb.cursor()
# data = [
#   (4, 'Pineapple','Yellow',20,'Chennai'),
#   (5, 'Mango','Yellow',25,'Hyderabad')
# ]
# stmt = "INSERT INTO Fruit_Details (fruit_id, name, color, cost, city) VALUES (%s,%s,%s,%s,%s)"
# mycursor.executemany(stmt, data)

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1@Mysql#4",
    database="sayur_class"
)
mycursor = mydb.cursor()
# mycursor.execute("create table Cafe_menu(Item varchar(100), Quantity int, Price int)")
# mydb.commit()
mycursor.execute("insert into Cafe_menu values('Idli',100,10)")
mycursor.execute("insert into Cafe_menu values('Vadai',30,5) ")
mycursor.execute("insert into Cafe_menu values('Tea',150,15)")
mydb.commit()
mycursor.execute("select * from Cafe_menu")
result=mycursor.fetchall()
for i in result:
    print(i)