import mysql.connector

# database connection
mydb = mysql.connector.connect(host="localhost", user="root", password="pass11", database= "youtube_db", auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

# Query for creating table
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

cursor.execute(ArtistTableSql)

# some other statements  with the help of cursor
mydb.close()
