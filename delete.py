import pymysql

# 连接 Mysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 删除
cursor.execute('delete from admin where id=%s',[1,])

conn.commit()

# 关闭连接                                                          
cursor.close()
conn.close()