import pymysql

db=pd.read_sql_query("select*from management",pymysql.connect(host="localhost",user="root",password="",db="axisflexicap"))

