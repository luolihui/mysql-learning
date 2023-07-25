from flask import Flask,render_template,request
import pymysql

app=Flask(__name__)

@app.route("/adduser",methods=['GET','POST'])
def add_user():
    if request.method=='GET':
        return render_template("add_user.html")
    
    username=request.form.get("user")
    password=request.form.get("pwd")
    mobile=request.form.get("mobile")

    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    

    sql='insert into admin(username,password,mobile) values(%s,%s,%s)'
    cursor.execute(sql,[username,password,mobile])
    conn.commit()

    # 关闭连接                                                          
    cursor.close()
    conn.close()

    return '添加成功'

@app.route('/showuser')
def show_user():
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='l1354866',db='unicom',charset='utf8')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    

    sql='select * from admin'
    cursor.execute(sql)
    data_list=cursor.fetchall()

    # 关闭连接                                                          
    cursor.close()
    conn.close()

    return render_template('show_user.html',data_list=data_list)

if __name__ == "__main__":
    app.run()