from flask import Flask
app = Flask(__name__)

@app.route('/')  # 什么样的URL能触发函数    根目录  /
def hello_world():
    return "今天天气真好，你说呢"

@app.route('/hello')  # /hello
def hello():
    return "hello world!"

if __name__ == '__main__':
    # app.run()
    # 调试模式：可事实修改脚本内容
    app.debug = True
    app.run()
