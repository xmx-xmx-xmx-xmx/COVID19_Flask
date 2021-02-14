from flask import Flask
from flask import request # 获取参数
from flask import render_template # 使用模板页面
app = Flask(__name__) # 创建flask实例，名叫app

# @app.route('/') # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
# def home():
#     return "zdhnb"



@app.route('/') 
def home1():
    # id = request.values.get("id")
    return f"""
    <form action = "/login">
        <!-- id: <input name = "name" value = {id}><br> -->
        id: <input name = "name"><br>
        password: <input name = "pwd">
        <input type = "submit">
    </form>
    """ 

@app.route('/login') # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
def home2():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    # return f"name = {name}, pwd = {pwd}"
    return render_template("index.html") # 返回页面

@app.route('/ajax', methods=["get","post"])
def home3():
    name = request.values.get("name")
    score = request.values.get("score")
    print(f"name:{name},score:{score}")
    return "dalao"

if __name__ == "__main__":
    app.run()