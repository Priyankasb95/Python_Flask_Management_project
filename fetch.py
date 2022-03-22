

import pymysql

import pandas as pd

db=pd.read_sql_query("select*from performance",pymysql.connect(host="localhost",user="root",password="",db="axisflexicap"))
print(db)


