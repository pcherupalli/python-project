import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        database="restaurant")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database:", err)

else:
    print("Connection established successfully")

# Displaying customer table details
cursor = conn.cursor()
cursor.execute("SELECT * FROM customer")
result = cursor.fetchall()
for row in result:
    print(row)
    print("\n")

# Inserting a new row
query = "insert into customer (Id,Phone_number,Passwrd,Mail_id) values (4,768889900,'hgfvbu','minnie@gmail.com');"
cursor = conn.cursor()
cursor.execute(query)
print(cursor.rowcount, "record added successfully")

# Deleting a row
mycursor = conn.cursor()
sql = "DELETE FROM customer WHERE Id = 4"
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "record deleted successfully")
conn.commit()
conn.close()











