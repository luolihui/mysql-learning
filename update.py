import pymysql

# 连接 Mysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 修改
cursor.execute('update admin set mobile=%s where id=%s',["1353272",4,])

conn.commit()

# 关闭连接                                                          
cursor.close()
conn.close()