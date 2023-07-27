import pymysql

def connect_mysql(host, port, user, password, database, charset):
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        print("Successfully connected to MySQL database")
        return conn
    except pymysql.Error as e:
        print("Failed to connect to MySQL database:", str(e))
        return None

def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Successfully executed the query:", query)
        cursor.close()
        return True
    except pymysql.Error as e:
        print("Failed to execute the query:", query)
        print("Error:", str(e))
        conn.rollback()
        return False

def execute_select(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        print("Successfully executed the SELECT query:", query)
        return results
    except pymysql.Error as e:
        print("Failed to execute the SELECT query:", query)
        print("Error:", str(e))
        return None

def disconnect_mysql(conn):
    try:
        conn.close()
        print("Successfully disconnected from MySQL database")
    except pymysql.Error as e:
        print("Failed to disconnect from MySQL database:", str(e))

# 示例用法：

# 连接到数据库
connection = connect_mysql('localhost', 3306, 'user', 'password', 'database_name', 'utf8')

# 执行插入操作
insert_query = "INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2')"
execute_query(connection, insert_query)

# 执行删除操作
delete_query = "DELETE FROM table_name WHERE condition"
execute_query(connection, delete_query)

# 执行更新操作
update_query = "UPDATE table_name SET column1 = 'new_value' WHERE condition"
execute_query(connection, update_query)
    
# 执行查询操作
select_query = "SELECT * FROM table_name"
results = execute_select(connection, select_query)

# 关闭数据库连接
disconnect_mysql(connection)

"""
# pip install dbutils
import threading
import pymysql
from dbutils.pooled_db import PooledDB

mysql_db_pool = PooledDB(
    creator = pymysql, # 使用连接数据库的模块
    maxconnections = 50, # 连接池允许的最大连接数，0表示不限制
    mincached = 2, # 初始化时，最少创建的空闲连接数
    maxcached = 3, # 最多闲置的连接数
    blocking = True, # 连接池中没有可用连接时，是否阻塞等待
    setsession = [], # 开始会话前执行的命令列表
    ping = 0,
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'l1354866',
    database = '数据库名',
    charset = 'utf8'
    )

def task():
    conn = mysql_db_pool.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.exceute('sql语句')
    result = cursor .fetchall()
    print(result)

    cursor.close()
    conn.close()

def run():
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
run()
"""
