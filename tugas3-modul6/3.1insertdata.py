import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",
                               password="", database="db_penjualan")
    # Membuat cursor
mycursor = mydb.cursor()
    # Query untuk menambahkan data
sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
val = ("1", "Food")
mycursor.execute(sql, val)

    # Commit perubahan
mydb.commit()

print(mycursor.rowcount, "Data Berhasil Ditambahkan")

