import streamlit as st
import mysql.connector
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
data = [["Channel_Name", "Test from test repo"],["Channel_Id", "UC1234567890",]]
st.table(data)

# Query for creating table
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

# database connection
mydb = mysql.connector.connect(host="192.168.56.1", user="root", password="pass11", database= "youtube_db", auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

if st.button("Upload to SQL"):
    with st.spinner('Please Wait for it...'):
        cursor.execute(ArtistTableSql)
        st.success("Upload to MogoDB successful !!")

# some other statements  with the help of cursor
mydb.close()
