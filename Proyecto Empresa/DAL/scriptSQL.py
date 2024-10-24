import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="gestion_empleados")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM empleado")

# Fetch one result
#row = cur.fetchone()
for filas in cur:
    print(filas)

# Close connection
cnx.close()