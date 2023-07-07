import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Nahida@123"
)


cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE IF NOT EXISTS nirab")


print("Database created successfully")