import mysql.connector

mysql_conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='dtvthe_test')

cusor = mysql_conn.cursor()

sql_query_select = 'SELECT * FROM hayvc'
sql_query_insert = 'INSERT INTO hayvc(name) VALUES ("Van Hoc")'

cusor.execute(sql_query_insert)


cusor.execute(sql_query_select)

for item in cusor:
    print(item)



cusor.close()
mysql_conn.close()