import streamlit as st
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
data = [["Channel_Name", "Test from test repo"],["Channel_Id", "UC1234567890",]]
st.table(data)

# Query for creating table
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

#db connection
try:
    mydb = mysql.connect(user='root',
                         password='pass11',
                         host='localhost',
                         port = 3306,
                         db= 'youtube_db',
                         auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    
except Error as error:
    print("error".format(error))
except Exception as e:
    print(e)
finally:
    if mydb.is_connected():
        print("Successful Connection")


if st.button("Upload to SQL"):
    with st.spinner('Please Wait for it...'):
        mycursor.execute(ArtistTableSql)
        st.success("Upload to MySQL successful !!")

# some other statements  with the help of cursor
mydb.close()
