import pymysql

while True:
    user = input("用户名：")
    if user.upper() == "Q":
        break
    pwd = input("密码：")
    mobile = input("手机号：")

    # 连接 Mysql，db为数据库
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 动态插入
    sql='insert into admin(username,password,mobile) values(%s,%s,%s)'
    cursor.execute(sql,[user,pwd,mobile])
    # 发送指令(3种静态方式)
    # sql='insert into admin(username,password,mobile) values("wupeiqi","qwe123","15122222222")'
    # cursor.execute(sql)

    # sql='insert into admin(username,password,mobile) values(%s,%s,%s)'
    # cursor.execute(sql,["汉朝","qwe123","13243744734"])

    # sql='insert into admin(username,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)'
    # cursor.execute(sql,{"n1":"萨哈","n2":"wer233","n3":"15272718193"})

    conn.commit()

    # 关闭连接                                                          
    cursor.close()
    conn.close()