import pymysql

# 连接 Mysql
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 发送查询指令，admin是 unicom数据库中的表
sql='select * from admin'
cursor.execute(sql)
data_list=cursor.fetchall()
for row_dict in data_list:
    print(row_dict)

# 关闭连接                                                          
cursor.close()
conn.close()

"""
create table adepart(
id int auto_increment primary key,
title varchar(16) not null
)default charset=utf8;
"""

"""
create table ainfo(
id int auto_increment primary key,
name varchar(16) not null,
email varchar(32),
age int,
depart_id int
)default charset=utf8;
"""

"""
select id,name,
       case when age<18 then "少年" end v1, 
       case when age<18 then "少年" else "青年" end v2, 
       case when age<18 then "少年" when age<30 the "青年" else "老年" end v3,
       case age when 18 then "刚成年" end v4,
       case age when 18 then "刚成年" else "其他" end v5
from ainfo;
"""
# SQL执行顺序：where ->group by ->having ->order by-> limit
"""
select * from ainfo where id>3 order by id desc limit 5;   -- 排序后取前5条数据
select * from ainfo limit 3 offset 2;  -- 从位置2开始，取后3条数据
select age,count(id) from ainfo where id>4 group by age having count(id)>2;
"""
