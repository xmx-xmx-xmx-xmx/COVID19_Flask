from flask import Flask
from flask import request # 获取参数
from flask import render_template # 使用模板页面
from flask import jsonify
import utils # 导入自己写的utils
app = Flask(__name__) # 创建flask实例，名叫app

# @app.route('/') # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
# def home():
#     return "zdhnb"

@app.route('/') 
# def home1():
#     # id = request.values.get("id")
#     return f"""
#     <form action = "/login">
#         <!-- id: <input name = "name" value = {id}><br> -->
#         id: <input name = "name"><br>
#         password: <input name = "pwd">
#         <input type = "submit">
#     </form>
#     """ 
def index():
    return render_template("main.html")

@app.route('/time') # 前端获取时间的那个
def get_time():
    return utils.get_time()

@app.route('/center1')
def get_center1_data():
    data = utils.get_center1_data() # 结果是元组
    return jsonify({"confirm":data[0], "suspect":data[1], "heal":data[2], "dead":data[3]})
# @app.route('/login') # 使用 route() 装饰器来告诉 Flask 触发函数的 URL
# def home2():
#     name = request.values.get("name")
#     pwd = request.values.get("pwd")
#     # return f"name = {name}, pwd = {pwd}"
#     return render_template("index.html") # 返回页面

# @app.route('/ajax', methods=["get","post"])
# def home3():
#     name = request.values.get("name")
#     score = request.values.get("score")
#     print(f"name:{name},score:{score}")
#     return "dalao"

@app.route('/center2')
def get_center2_data():
    res = []
    for tup in utils.get_center2_data(): # 遍历
        print(tup)
        res.append({"name":tup[0],"value":int(tup[1])}) # 拼装成dict 追加到res
    return jsonify({"data":res}) # json化输出

if __name__ == "__main__":
    app.run()