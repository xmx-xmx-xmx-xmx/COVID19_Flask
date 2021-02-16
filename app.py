from flask import Flask
from flask import json
from flask import request # 获取参数
from flask import render_template # 使用模板页面
from flask import jsonify
from jieba.analyse import extract_tags # 解析标签
import utils # 导入自己写的utils
app = Flask(__name__) # 创建flask实例，名叫app

@app.route('/') # 默认路由
# def home1(): # 示例，写一个登陆页面
#     # id = request.values.get("id")
#     return f"""
#     <form action = "/login"> <!-- 这里面是html标记 -->
#         <!-- id: <input name = "name" value = {id}><br> -->
#         id: <input name = "name"><br>
#         password: <input name = "pwd">
#         <input type = "submit">
#     </form>
#     """ 
def index():
    return render_template("main.html") # 加载页面模板 main

@app.route('/time') # 前端获取时间的功能实现
def get_time():
    return utils.get_time() # 返回util.py中 get_time()的内容

@app.route('/center1')
def get_center1_data():
    data = utils.get_center1_data() # 结果是元组
    return jsonify({"confirm":data[0], "suspect":data[1], "heal":data[2], "dead":data[3]}) # json化输出

# @app.route('/login') # 使用 route() 装饰器来告诉 Flask 触发函数的 URL 例子：一个home页面，返回登录页例子输入的账号和密码
# def home2():
#     name = request.values.get("name")
#     pwd = request.values.get("pwd")
#     # return f"name = {name}, pwd = {pwd}"
#     return render_template("index.html") # 返回页面

# @app.route('/ajax', methods=["get","post"]) # 传输账号密码的ajax请求
# def home3():
#     name = request.values.get("name")
#     score = request.values.get("score")
#     print(f"name:{name},score:{score}")
#     return "dalao"

@app.route('/center2') # 地图展示
def get_center2_data():
    res = []
    for tup in utils.get_center2_data(): # 遍历
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])}) # 拼装成dict 追加到res
    return jsonify({"data":res}) # json化输出

@app.route('/left1') # 左1图表
def get_left1_data():
    data = utils.get_left1_data()
    day, confirm, suspect, heal, dead = [],[],[],[],[]
    for a, b, c, d, e in data: # [7:]第八条开始
        day.append(a.strftime("%m.%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day, "confirm":confirm, "suspect":suspect, "heal":heal, "dead":dead})

@app.route('/left2') #左2图表
def get_left2_data():
    data = utils.get_left2_data()
    ds, confirm_add, suspect_add = [],[],[]
    for a, b, c in data:
        ds.append(a.strftime("%m.%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"ds":ds, "confirm_add":confirm_add, "suspect_add":suspect_add})

@app.route('/right1') #右1图表
def get_right1_data():
    data = utils.get_right1_data()
    city = []
    confirm =[]
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city":city, "confirm":confirm})

# @app.route('/right2') #右2 弃用
# def get_right2_data():
#     data = utils.get_right2_data()
#     info = []
#     for k in data:
#         i = k.replace('｜','') # 删除|
#         tag = extract_tags(i) # jieba提取关键字
#         for j in tag:
#             info.append({"info":j})
#     return jsonify({"kws":info})

if __name__ == "__main__": # main
    app.run()