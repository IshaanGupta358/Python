
import mysql.connector

db = mysql.connector.connect(host='localhost', password='2009', user='root')



try:
    cursor = db.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM database_ishaan.students")
    result = cursor.fetchone()      
    row_count = result[0]
    r_no = row_count + 1
   

except Exception as e:
    print(e)

    db.rollback()



