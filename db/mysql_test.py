import mysql.connector

cnx = mysql.connector.connect(user='scott', password='tiger',
                              host='127.0.0.1',
                              database='3semi2021')
cur = cnx.cursor(dictionary=True)

#cur.execute("SELECT sal, ename FROM emp")
cur.execute("SELECT * FROM emp")
#print(cur.fetchall())

for row in cur:
    #print(row["ename"], row["sal"])
    print(row["ENAME"])

cur.close()

cnx.close()